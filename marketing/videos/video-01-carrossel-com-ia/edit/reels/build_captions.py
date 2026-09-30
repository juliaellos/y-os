"""Legendas do Reels: transcrição Whisper -> chunks no timeline de saída.

Gera animations/slot_3/captions.js (dados da composição) e master.srt.
O timeline de saída tem +0.2s de respiro inserido no corte da cena 1 pra 2,
então toda palavra depois do corte anda 0.2s.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
EDL = json.loads((HERE / "edl.json").read_text())
SHIFT_AFTER = EDL["breath"]["caption_shift_after_s"]  # palavras que começam depois disso andam
SHIFT = EDL["breath"]["seconds"]
END_SEGMENT_OUT = EDL["layout"]["end_segment_out_s"]
OUT_DUR = EDL["output"]["duration"]

# Chunks escritos com os tokens crus da transcrição, na ordem. O script confere
# token por token, então um erro de digitação aqui quebra em vez de desalinhar.
CHUNKS = [
    "Esse carrossel aqui",
    "eu não fiz com o Canva,",
    "eu não contratei designer,",
    "eu fiz tudo com",
    "inteligência artificial,",
    "com o Cloud,",
    "levou mais ou menos",
    "10 minutos.",
    "Vocês provavelmente",
    "já vieram aqui",
    "no Gemini, no chat GPT,",
    "pediram para eles",
    "criarem um carrossel",
    "para vocês",
    "e no final",
    "eles entregaram textos",
    "que tu precisou copiar,",
    "levar para o Canva",
    "e fazer toda a edição",
    "do carrossel manual.",
    "Com o Cloud Code",
    "isso é diferente,",
    "porque ele já está",
    "conectado direto",
    "na pasta do teu computador,",
    "tu vai fazer o pedido",
    "para ele",
    "e no final ele vai",
    "te entregar",
    "as imagens prontas",
    "para te postar",
    "no teu Instagram.",
    "O prompt que eu usei,",
    "ele já está pronto para ti,",
    "você só precisa mandar",
    "a palavra carrossel",
    "na minha DM do Instagram,",
    "só vai precisar alterar",
    "o tema e as cores",
    "do teu carrossel.",
]

# Correções de grafia (Whisper escreve "Cloud" e separa "chat GPT").
FIX = {"Cloud": "Claude", "Cloud,": "Claude,"}
MERGE = {("chat", "GPT,"): "ChatGPT,"}

# Palavras em verde-limão: só a promessa e a virada, nunca a parte do problema
# (Gemini, ChatGPT, Canva ficam brancos), seguindo a narrativa de cor do guia.
LIME = {
    (5, "Claude"),
    (7, "10"), (7, "minutos"),
    (20, "Claude"), (20, "Code"),
    (29, "imagens"), (29, "prontas"),
    (35, "carrossel"),
}


def out_t(t):
    return round(t + SHIFT, 3) if t >= SHIFT_AFTER else round(t, 3)


def main():
    raw = json.loads((HERE / "transcripts/01-meu-carrossel-reels.json").read_text())["words"]
    words = [w for w in raw if w["type"] == "word"]
    i = 0
    chunks = []
    for ci, text in enumerate(CHUNKS):
        toks = text.split()
        ws = []
        k = 0
        while k < len(toks):
            w = words[i]
            assert w["text"] == toks[k], f"chunk {ci}: esperava {toks[k]!r}, veio {w['text']!r}"
            pair = tuple(toks[k:k + 2])
            if pair in MERGE:
                w2 = words[i + 1]
                assert w2["text"] == toks[k + 1]
                ws.append({"text": MERGE[pair], "start": w["start"], "end": w2["end"]})
                i += 2
                k += 2
                continue
            ws.append({"text": FIX.get(w["text"], w["text"]), "start": w["start"], "end": w["end"]})
            i += 1
            k += 1
        # Pontuação no fim do chunk sai: a quebra do chunk já é a pausa.
        ws[-1]["text"] = re.sub(r"[.,]$", "", ws[-1]["text"])
        chunk_words = []
        for w in ws:
            bare = re.sub(r"[.,]$", "", w["text"])
            chunk_words.append({
                "t": w["text"],
                "s": out_t(w["start"]),
                "e": out_t(w["end"]),
                "lime": (ci, bare) in LIME,
            })
        chunks.append({"words": chunk_words})
    assert i == len(words), f"sobraram {len(words) - i} palavras"

    for ci, c in enumerate(chunks):
        c["start"] = c["words"][0]["s"]
        nxt = chunks[ci + 1]["words"][0]["s"] if ci + 1 < len(chunks) else OUT_DUR
        c["end"] = round(min(nxt, c["words"][-1]["e"] + 0.35), 3)
        c["pos"] = "chest" if c["start"] >= END_SEGMENT_OUT else "seam"
        if c["pos"] == "seam":
            # No trecho final a câmera sobe e a posição da emenda cai na testa dela.
            c["end"] = min(c["end"], END_SEGMENT_OUT)
    chunks[0]["start"] = 0.0  # primeiro quadro já com legenda: é o gancho
    chunks[-1]["end"] = OUT_DUR
    # "10 minutos" some antes do zoom da transição começar a borrar a imagem.
    chunks[7]["end"] = round(chunks[7]["words"][-1]["e"] + 0.08, 3)

    js = "window.CAPTIONS = " + json.dumps(chunks, ensure_ascii=False, indent=1) + ";\n"
    (HERE / "animations/slot_3/captions.js").write_text(js)

    def ts(t):
        ms = int(round(t * 1000))
        return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"

    srt = []
    for n, c in enumerate(chunks, 1):
        line = " ".join(w["t"] for w in c["words"])
        srt.append(f"{n}\n{ts(c['start'])} --> {ts(c['end'])}\n{line}\n")
    (HERE / "master.srt").write_text("\n".join(srt))
    print(f"{len(chunks)} chunks, {sum(len(c['words']) for c in chunks)} palavras")
    for c in chunks:
        line = " ".join(("*" + w["t"] + "*") if w["lime"] else w["t"] for w in c["words"])
        print(f"{c['start']:6.2f}-{c['end']:6.2f} [{c['pos']}] {line}")


if __name__ == "__main__":
    main()
