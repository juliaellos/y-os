"""Monta o Reels a partir do edl.json.

Por quadro, em RGB (sem conversão de cor do ffmpeg no meio do caminho):
  1. troca o preto e a sombra por #16141F nos trechos vazios
  2. sobrepõe o leque (slot_1)
  3. zoom com desfoque na emenda da cena 1 pra 2 (+0.2s de respiro)
  4. sobrepõe o card do final (slot_2)
  5. legendas por último (slot_3)
Áudio: respiro de 0.2s no corte, fades de 30ms, efeitos sonoros, limitador.

Uso:
  python3 compose.py                       # final.mp4
  python3 compose.py --stills 0,120,250    # só PNGs desses quadros em previas/
"""
import argparse
import json
import os
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).parent
# Quadros das animações e áudio intermediário ficam fora do iCloud: a Mesa
# sincroniza e, com o disco cheio, o macOS despeja arquivos recém-criados pra
# nuvem ("dataless"). Ler de volta trava o render. REELS_WORK aponta pra uma
# pasta local; sem ela, usa a própria pasta do projeto.
WORK = Path(os.environ.get("REELS_WORK", HERE))
EDL = json.loads((HERE / "edl.json").read_text())
W, H = EDL["output"]["width"], EDL["output"]["height"]
FPS = EDL["fps"]
N_OUT = EDL["output"]["frames"]
SR = 48000

BR = EDL["breath"]
CUT_SRC = BR["src_cut_frame"]  # primeiro quadro da cena 2 no original
FB, FA = BR["freeze_before"], BR["freeze_after"]
SHIFT_FRAMES = FB + FA


def src_frame(n):
    """Quadro do original que aparece no quadro n da saída."""
    if n < CUT_SRC:
        return n
    if n < CUT_SRC + FB:
        return CUT_SRC - 1
    return max(CUT_SRC, n - SHIFT_FRAMES)


# ---------- 1. fundo e sombra ----------

def smoothstep(y, y0, y1):
    x = np.clip((y - y0) / (y1 - y0), 0, 1)
    return x * x * (3 - 2 * x)


COLOR = np.array(EDL["recolor"]["color"], np.float32)
LIFTS = []
for seg in EDL["recolor"]["segments"]:
    shadow = 1 - smoothstep(np.arange(H, dtype=np.float32), seg["y0"], seg["y1"])
    lift = np.rint(shadow[:, None, None] * COLOR[None, None, :]).astype(np.int16)
    rows = int(np.nonzero(shadow > 0)[0].max()) + 1
    LIFTS.append((seg["src_frames"][0], seg["src_frames"][1], lift[:rows], rows))


def recolor(frame, s):
    for a, b, lift, rows in LIFTS:
        if a <= s <= b:
            top = frame[:rows].astype(np.int16) + lift
            frame[:rows] = np.clip(top, 0, 255).astype(np.uint8)
    return frame


# ---------- overlays ----------

SLOTS = {o["slot"]: o for o in EDL["overlays"]}


def overlay(frame, slot, n):
    o = SLOTS[slot]
    k = n - o["out_start_frame"]
    if not (0 <= k < o["frames"]):
        return frame
    path = WORK / f"animations/{slot}/renders/frames/frame_{k + 1:06d}.png"
    im = Image.open(path)
    im.load()
    box = im.getchannel("A").getbbox()
    if box is None:
        return frame
    x0, y0, x1, y1 = box
    ov = np.asarray(im.crop(box).convert("RGBA"), np.float32)
    a = ov[..., 3:4] / 255.0
    base = frame[y0:y1, x0:x1].astype(np.float32)
    frame[y0:y1, x0:x1] = np.clip(base * (1 - a) + ov[..., :3] * a + 0.5, 0, 255).astype(np.uint8)
    return frame


# ---------- 3. zoom com desfoque ----------

TR = EDL["transition"]


def zoom_params(n):
    i0, i1 = TR["in_frames"]
    o0, o1 = TR["out_frames"]
    smax, bmax = TR["max_scale"] - 1, TR["max_blur"]
    if i0 <= n <= i1:  # acelera pra dentro até o corte
        p = (n - i0 + 1) / (i1 - i0 + 1)
        return 1 + smax * p ** 2, bmax * p ** 2
    if o0 <= n <= o1:  # sai de perto e assenta
        q = 1 - (n - o0) / (o1 - o0 + 1)
        return 1 + smax * q ** 3, bmax * q ** 3
    return None


def zoom_blur(frame, scale, blur):
    cx, cy = TR["center"]
    img = Image.fromarray(frame)
    samples = 9 if blur > 0.004 else 1
    acc = np.zeros((H, W, 3), np.float32)
    for j in range(samples):
        f = scale * (1 + blur * j / max(1, samples - 1))
        hw, hh = W / (2 * f), H / (2 * f)
        box = (cx - hw, cy - hh, cx + hw, cy + hh)
        acc += np.asarray(img.resize((W, H), Image.BILINEAR, box=box), np.float32)
    return np.clip(acc / samples + 0.5, 0, 255).astype(np.uint8)


# ---------- quadro completo ----------

def build_frame(n, src):
    s = src_frame(n)
    frame = recolor(src.copy(), s)
    frame = overlay(frame, "slot_1", n)
    zp = zoom_params(n)
    if zp:
        frame = zoom_blur(frame, *zp)
    frame = overlay(frame, "slot_2", n)
    frame = overlay(frame, "slot_3", n)
    return frame


def decode_source():
    cmd = [
        "ffmpeg", "-v", "error", "-i", EDL["source"], "-an",
        "-vf", "scale=1080:1920:flags=lanczos+accurate_rnd+full_chroma_int"
               ":in_color_matrix=bt709:in_range=tv,format=rgb24",
        "-f", "rawvideo", "-",
    ]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=W * H * 3 * 4)
    size = W * H * 3
    while True:
        buf = p.stdout.read(size)
        if len(buf) < size:
            break
        yield np.frombuffer(buf, np.uint8).reshape(H, W, 3)
    p.wait()


def check_frame_count(path):
    n = subprocess.run(
        ["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0",
         "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    assert int(n) == N_OUT, f"{path} saiu com {n} quadros, esperado {N_OUT}"


def frames(limit=N_OUT):
    """(n, quadro do original) na ordem da saída, lendo o vídeo uma vez só."""
    src_iter = decode_source()
    cur_idx, cur = -1, None
    for n in range(limit):
        s = src_frame(n)
        while cur_idx < s:
            cur = next(src_iter)
            cur_idx += 1
        yield n, cur


# ---------- áudio ----------

def load_audio(path, extra=()):
    cmd = ["ffmpeg", "-v", "error", *extra, "-i", str(path), "-vn", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def fade(x, n_in=0, n_out=0):
    if n_in:
        x[:n_in] *= np.linspace(0, 1, n_in, dtype=np.float32)[:, None]
    if n_out:
        x[-n_out:] *= np.linspace(1, 0, n_out, dtype=np.float32)[:, None]
    return x


def flick(seed, peak_db):
    """Estalo curto de carta: ruído filtrado 1.8-7 kHz com decaimento rápido."""
    rng = np.random.default_rng(seed)
    n = int(0.06 * SR)
    noise = rng.standard_normal(n).astype(np.float32)
    spec = np.fft.rfft(noise)
    fr = np.fft.rfftfreq(n, 1 / SR)
    spec[(fr < 1800) | (fr > 7000)] = 0
    x = np.fft.irfft(spec, n).astype(np.float32)
    t = np.arange(n) / SR
    env = np.minimum(t / 0.0015, 1) * np.exp(-t / 0.012)
    x *= env.astype(np.float32)
    x *= 10 ** (peak_db / 20) / (np.abs(x).max() + 1e-9)
    pan = 0.5 + 0.25 * rng.uniform(-1, 1)
    return np.stack([x * (1 - pan) * 2 ** 0.5, x * pan * 2 ** 0.5], axis=1)


def build_audio():
    fade_n = int(EDL["audio_fade_ms"] / 1000 * SR)
    src = load_audio(EDL["source"])
    split = int(round(BR["audio_split_s"] * SR))
    a = fade(src[:split].copy(), n_out=fade_n)
    b = fade(src[split:].copy(), n_in=fade_n)
    gap = np.zeros((int(round(BR["seconds"] * SR)), 2), np.float32)
    mix = np.concatenate([a, gap, b])
    total = int(round(N_OUT / FPS * SR))
    mix = np.pad(mix, ((0, max(0, total - len(mix))), (0, 0)))[:total]

    sfx_dir = Path(EDL["sfx_dir"])
    for e in EDL["sfx"]:
        if e["file"] == "synth:flick":
            for k, at in enumerate(e["at"]):
                clip = flick(k, e["peak_dbfs"])
                i = int(round(at * SR))
                mix[i:i + len(clip)] += clip[: total - i]
            continue
        extra = []
        if "offset" in e:
            extra += ["-ss", str(e["offset"])]
        if "dur" in e:
            extra += ["-t", str(e["dur"])]
        clip = load_audio(sfx_dir / e["file"], extra)
        if "dur" in e:
            clip = fade(clip, n_in=int(0.01 * SR), n_out=int(0.06 * SR))
        clip *= 10 ** (e["gain_db"] / 20)
        i = int(round(e["at"] * SR))
        j = min(total, i + len(clip))
        mix[i:j] += clip[: j - i]

    (WORK / "audio").mkdir(parents=True, exist_ok=True)
    pre = WORK / "audio/mix_pre.f32"
    pre.write_bytes(mix.astype(np.float32).tobytes())
    limit = 10 ** (EDL["limiter_db"] / 20)
    out = WORK / "audio/mix.wav"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", str(pre),
        "-af", f"alimiter=limit={limit:.4f}:attack=5:release=60:level=0",
        "-c:a", "pcm_s24le", str(out),
    ], check=True)
    pre.unlink()
    return out


# ---------- saída ----------

def render(out_path):
    wav = build_audio()
    enc = subprocess.Popen([
        "ffmpeg", "-v", "error", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-i", str(wav),
        "-map", "0:v", "-map", "1:a",
        # setparams: sem ele o arquivo sai com primaries/transfer "unknown" e
        # player que chuta BT.601 mostra o verde-limão como (200,255,60).
        "-vf", "scale=out_color_matrix=bt709:out_range=tv:flags=accurate_rnd+full_chroma_int,format=yuv420p,"
               "setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv",
        "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-profile:v", "high",
        "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        str(out_path),
    ], stdin=subprocess.PIPE)
    for n, src in frames():
        enc.stdin.write(build_frame(n, src).tobytes())
        if n % 150 == 0:
            print(f"  quadro {n}/{N_OUT}", flush=True)
    enc.stdin.close()
    assert enc.wait() == 0, "ffmpeg falhou no encode"
    check_frame_count(out_path)
    print("ok:", out_path)


def stills(which):
    want = sorted(set(which))
    outdir = HERE / "previas"
    outdir.mkdir(exist_ok=True)
    for n, src in frames(want[-1] + 1):
        if n in want:
            Image.fromarray(build_frame(n, src)).save(outdir / f"q{n:04d}.png")
    print("stills:", [f"q{n:04d}.png" for n in want])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stills", help="quadros da saída, separados por vírgula")
    ap.add_argument("--audio-only", action="store_true")
    ap.add_argument("-o", default=str(HERE / "final.mp4"))
    args = ap.parse_args()
    if args.stills:
        stills([int(x) for x in args.stills.split(",")])
    elif args.audio_only:
        print("ok:", build_audio())
    else:
        render(args.o)
