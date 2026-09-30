"""Renderiza as legendas (slot_3) em 3 pedaços e junta num PNG sequence só.

O HyperFrames confere o disco antes de um png-sequence estimando o quadro
sem compressão (~8 MB cada): 1207 quadros pedem ~10 GB livres, mesmo que os
PNGs reais somem ~40 MB. Em pedaços de ~402 quadros a conta cabe.

Uso: REELS_WORK=<pasta local> python3 render_captions.py
"""
import os
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
SLOT = HERE / "animations/slot_3"
WORK = Path(os.environ.get("REELS_WORK", HERE))
OUT = WORK / "animations/slot_3/renders/frames"
FPS = 30
N = 1207
CUTS = [0, 403, 805, N]  # quadro inicial de cada pedaço

base = (SLOT / "index.html").read_text()
assert base.count('data-duration="40.2333"') == 2
REG = 'window.__timelines["legendas-reels"] = tl;'
assert REG in base

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

for i in range(3):
    f0, f1 = CUTS[i], CUTS[i + 1]
    start, dur = f0 / FPS, (f1 - f0) / FPS
    html = base.replace('data-duration="40.2333"', f'data-duration="{dur:.6f}"')
    # Um timeline por cima que só arrasta o timeline completo de start a
    # start+dur: o pedaço mostra exatamente aquele trecho, seek-safe.
    html = html.replace(REG, (
        f"const seg = gsap.timeline({{ paused: true }});\n"
        f"      seg.add(tl.tweenFromTo({start:.6f}, {start + dur:.6f}, "
        f"{{ ease: \"none\", duration: {dur:.6f} }}), 0);\n"
        f"      window.__timelines[\"legendas-reels\"] = seg;"
    ))
    seg_html = SLOT / f"index-seg{i + 1}.html"
    seg_html.write_text(html)
    tmp = WORK / f"animations/slot_3/seg{i + 1}"
    if tmp.exists():
        shutil.rmtree(tmp)
    try:
        subprocess.run(
            ["npx", "--yes", "hyperframes", "render", "-c", seg_html.name,
             "--format", "png-sequence", "--workers", "1", "-o", str(tmp), "--quiet"],
            cwd=SLOT, check=True, capture_output=True,
        )
    finally:
        seg_html.unlink()
    frames = sorted(tmp.glob("frame_*.png"))
    assert len(frames) == f1 - f0, f"pedaço {i + 1}: {len(frames)} quadros, esperado {f1 - f0}"
    for k, p in enumerate(frames):
        p.rename(OUT / f"frame_{f0 + k + 1:06d}.png")
    shutil.rmtree(tmp)
    print(f"pedaço {i + 1}: quadros {f0}-{f1 - 1} ok")

print("total:", len(list(OUT.glob("frame_*.png"))))
