# Prompts de imagem — carrossel "Como eu crio carrossel com IA (sem app)"

> Estilo de referência: fotografia editorial de moda, luz de estúdio,
> pose controlada, colidida com um elemento surreal literal que
> materializa a metáfora do texto do slide (linha da ELLOS: tubarões,
> iceberg, ovelha azul, tabuleiro de xadrez, celular gigante, casaco-
> tentáculo). Sempre fotorrealista, nunca ilustração/render 3D
> estilizado. Rodar cada prompt no Gemini e salvar como
> `foto-slide-0X.png` nesta pasta.
>
> **Distribuição neste carrossel (teste em 2026-09-14):** imagem
> conceitual só na capa (slide 1) e no CTA final (slide 8). Os 6 slides
> internos ficam texto puro — decisão pra variar o ritmo e harmonizar a
> grade do feed, não repetir imagem em todo slide.

## Slide 1 — CAPA (versão 1, aprovada e substituída)
**Metáfora:** criar sozinha, sem depender de ferramenta pronta = construir com as próprias mãos, não pegar algo pronto na prateleira
**Prompt:**
```
Editorial fashion photography of a woman in a tailored dark suit standing in a minimalist studio, holding a small handheld printing press or letterpress machine against her chest, ink-stained hands, dramatic single-source studio lighting, neutral dark grey background, shot from a low angle, high-fashion editorial aesthetic, shallow depth of field, sharp focus on her face and the press, muted color grading with a single lime-green accent light, editorial quality, photorealistic
```
Resultado: boa, mas sem pessoa foi decidido melhor pra capa — ver versão 2 abaixo.

## Slide 1 — CAPA (versão 2, em uso)
**Metáfora:** carrossel físico (brinquedo) = carrossel de Instagram. Um
cavalinho iluminado em verde-limão entre os demais na sombra = a
diferenciação de fazer com identidade própria, não genérico. Moldura
luminosa flutuando sobre o cavalinho = conecta visualmente com formato
de post/story, sem colar ícone de app literal na cena.
**Prompt:**
```
Editorial still life photography of a miniature vintage carousel/merry-go-round made of dark metal and glass, sitting alone in a minimalist dark studio void, one of its horses glowing with lime-green light while the rest remain in shadow, a thin glowing lime-green square frame with rounded corners floating in the air just above the glowing horse, like a photo card or social media post outline made of light, dramatic single-source overhead lighting, neutral dark grey background, shallow depth of field, high-fashion editorial aesthetic, muted color grading, photorealistic, editorial quality
```

## Slides 2 a 7 — texto puro
Sem imagem conceitual neste carrossel. Layout permanece SOLO/NÚMERO/
CITAÇÃO só com tipografia, como já renderizado.

## Slide 8 — CTA final (convite pro YouTube)
**Metáfora:** abrir uma porta pro próximo passo, convite literal
**Prompt:**
```
Editorial fashion photography of a woman in a dark tailored outfit opening a large solid lime-green door standing alone in an empty minimalist studio void, warm light spilling through the doorway from the other side, neutral dark background, high-fashion editorial aesthetic, shallow depth of field, photorealistic, editorial quality
```

---

## Depois de gerar as imagens
Trocar `<div class="face-panel">` / equivalentes no `carrossel.html` por
`<img>` com cada `foto-slide-0X.png`, com gradient overlay
`linear-gradient(rgba(22,20,31,0.55), rgba(22,20,31,0.85))` por cima pra
manter o texto legível, como já documentado na skill `/carrossel`.
