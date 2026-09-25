# Carrossel v2: Como eu crio carrossel com IA (sem Canva)

> Versão 2, 2026-09-24. 7 slides. A v1 (5 slides) continua na pasta de
> cima, sem alteração.

**Ideia central:** quase todo mundo faz carrossel pedindo o texto pro
ChatGPT e montando no Canva, o que dá trabalho ou sai com cara de IA.
Quando você conversa com uma IA que cria os arquivos e decide cada parte,
ele sai pronto e com a sua cara, e o vídeo mostra como.

**Sem @ em nenhum slide** (o perfil já aparece no post). Sem contagem de slides.

**Logo:** centralizada no topo na capa e no CTA; no canto inferior direito nos slides 2 a 6.

**Narrativa visual:** o verde-limão só aparece quando a pessoa passa a
decidir. O slide 2 (o caminho de sempre) fica sem verde nenhum; do 3 em
diante a luz acende. Os slides 2 e 3 formam um antes e depois na mesma
altura da tela: o fluxo cinza "ChatGPT → copia e cola → Canva → slide por
slide, na mão", e depois uma conversa curta em que a pessoa só pede e
aprova. Grão em todos os slides internos, pra conversar com o estúdio
escuro das fotos.

## Slide 1: Capa (foto do carrossel com o cavalo verde)
**Kicker:** TUTORIAL
**Título:** Como eu crio / carrossel com IA (sem Canva)
**Subtítulo:** Um jeito de usar o Claude que deixa você decidir cada detalhe do post.

## Slide 2: O problema (fluxo ChatGPT → Canva em cinza, 3 de 6 slides montados)
**H2:** Quase todo mundo faz / carrossel no ChatGPT
**Corpo:** Ele escreve o texto, você cola no Canva e monta slide por slide na mão. E quando pede a imagem pronta, ela vem com aquela cara de IA que todo mundo já reconhece no feed.

## Slide 3: O que eu faço no lugar (conversa com o Claude)
**H2:** Eu converso com a IA e decido cada detalhe
**Corpo:** Uso o Claude Code, uma IA que cria os arquivos direto no computador. Eu explico o que quero como explicaria pra uma designer, e ela devolve as imagens prontas.
**Conversa:**
- Você: deixa o título da capa mais direto
- Claude: Pronto, ficou assim: "Como eu crio carrossel com IA (sem Canva)". Posso montar as imagens?
- Você: pode

## Slide 4: Como funciona (passos ligados por linha verde)
**H2:** Do zero ao post pronto, em três passos
1. Você abre o Claude Code numa pasta nova do seu computador.
2. Escreve um prompt com o tema, o público e o visual que quer: as suas cores, as suas fontes e o estilo.
3. Lê o texto de cada slide e ajusta o que quiser antes de a IA montar as imagens.

## Slide 5: A prova (miniaturas reais dos 7 slides, o 5º aceso)
**H2:** Este carrossel foi feito desse jeito
**Corpo:** As cores, as fontes e todas as frases que você leu até aqui passaram pela minha aprovação. O Claude ficou com o trabalho de montar e exportar cada imagem.

## Slide 6: Frase de destaque (sem aspas, antes do CTA)
**Frase:** Parece feito à mão porque foi você quem decidiu cada linha ("foi você quem decidiu" em verde)
**Apoio:** e é isso que faz alguém parar no seu post no meio do feed

## Slide 7: CTA (foto da porta verde, logo centralizado no topo)
**Headline:** O passo a passo completo tá no meu YouTube
**Apoio:** Com a tela gravada do começo ao fim e o prompt que eu uso, pronto pra copiar.
**Botão:** Link na bio

## Arquivos
- `carrossel.html` + `render.js` (duas passadas: o slide 5 usa os PNGs dos outros slides)
- Render: `NODE_PATH="../../STAND_BY_carrossel-tempo-economizado-2026-09-16/node_modules" node render.js`
- Fotos: `foto-capa.jpg` (cópia de `../foto-slide-01-1.jpg`), `foto-cta.jpg` (cópia de `../foto-slide-05.JPG`)
