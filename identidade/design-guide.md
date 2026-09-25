# Identidade visual

> Como a marca aparece em tudo que o MazyOS gera.
> As skills de conteúdo, carrossel e post leem esse arquivo antes de criar qualquer visual.
> Edite quando a marca evoluir.

---

## Cores

- **Fundo principal:** #16141F (roxo quase-preto)

- **Cor de destaque / CTA:** #C6F135 (verde-limão)

- **Texto principal:** #F2F0F5 (branco levemente quente)

- **Fundo alternativo / cards:** #201D2E

- **Cor de marca / acento secundário:** #5B3FA0 (roxo)

- **Cor proibida:** amarelo (#F2C94C). Testado e descartado em favor do verde-limão

---

## Tipografia

- **Títulos e destaques:** Space Grotesk (Google Fonts)

- **Corpo, subtítulos e botões:** Inter (Google Fonts)

- **Peso do título:** 700 (bold)

---

## Estilo geral

Fundo escuro como padrão (dark-first), não claro. Tom tech e direto, sem
ilustração nem elemento decorativo: a identidade se sustenta em
tipografia, cor de destaque e espaço em branco (negativo). Contraste alto
entre fundo roxo-escuro e o verde-limão de destaque, usado com moderação
(CTA, links, poucos elementos por peça — nunca como cor de fundo grande).

Desde o post 1 v2 (2026-09-24), o fundo escuro ganhou atmosfera: grão
fino em todos os slides internos e luz difusa (verde ou roxa) atrás do
elemento principal, pra conversar com o estúdio escuro das fotos. A
referência completa está em "Padrão de referência: carrossel v2", abaixo.

## Elementos-chave

- Bordas: 1px, cor `#2a2636` (mistura de fundo alternativo com um pouco
  de luz). Usar com moderação, preferir espaço em branco a separar com
  linha
- Border-radius dos cards: 12-14px
- Botões: preenchido com verde-limão (`#C6F135`) + texto `#16141F` pro CTA
  principal; contorno roxo (`#5B3FA0`) + texto verde-limão pro secundário
- Sombras: evitar. Se precisar separar camada, usar fundo alternativo
  (`#201D2E`) em vez de sombra. Luz difusa (glow radial) é permitida e
  faz parte do padrão v2, porque ilumina em vez de separar camada

---

## Padrão de referência: carrossel v2 (aprovado em 2026-09-24)

**Referência viva:** `marketing/conteudo/carrossel-carrossel-com-ia-2026-09-14/v2/`
(`carrossel.html` + PNGs em `instagram/`). Post 1, publicado em
2026-09-24. Todo carrossel novo parte daqui: copiar as classes do HTML
em vez de reinventar.

### Narrativa de cor

- O verde-limão só acende quando a pessoa passa a decidir, ou seja, no
  slide em que a solução aparece. Até ali, tudo fica em branco e cinza.
- Slide do problema (o jeito de sempre): kicker e régua em cinza
  (`.muted`), nenhum verde na tela.
- Da virada em diante: kicker verde, régua verde e luz verde atrás do
  elemento principal.
- Slide de frase de destaque: só o trecho que carrega a ideia fica em
  verde (ex: "Parece feito à mão porque **foi você quem decidiu** cada
  linha").

### Fundos e textura

- Slides internos alternam `#16141F` e `#201D2E`.
- Atrás das fotos (capa e CTA), fundo quase preto quente (`#14120d` /
  `#1a140e`), pra casar com a luz de estúdio da foto.
- **Grão** em todos os slides internos (nunca na capa nem no CTA com
  foto). Camada `::after` com ruído SVG, opacidade 0.13:
  ```css
  .grain::after { content:""; position:absolute; inset:0; z-index:1;
    pointer-events:none; opacity:0.13;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23n)'/%3E%3C/svg%3E"); }
  ```
- **Luz verde** (`.glow-lime` / `.halo`): radial de `rgba(198,241,53,0.22-0.30)`
  até transparente, atrás do elemento que representa a solução
  (conversa, grade de prova).
- **Luz roxa** (`.glow-purple`): radial de `rgba(91,63,160,0.55)` até
  transparente, grande e vazando pela lateral. Usada no slide de frase.
- **Grade técnica** (`.blueprint`): linhas de 1px a 4% de opacidade, a
  cada 90px, com máscara radial pra sumir nas bordas. Usada no slide de
  passos.
- Uma luz por slide, no máximo.

### Escala de tipo (1080x1350)

| Elemento | Fonte | Tamanho | Detalhe |
|---|---|---|---|
| Título da capa | Space Grotesk 700 | 74px | line-height 1.02, letter-spacing -0.03em. Complemento entre parênteses a 36px |
| H2 dos slides internos | Space Grotesk 700 | 64px | line-height 1.05, letter-spacing -0.03em |
| Frase de destaque | Space Grotesk 700 | 74px | line-height 1.1, sem aspas |
| Headline do CTA | Space Grotesk 700 | 56px | centralizada |
| Kicker | Space Grotesk 700 | 15px | caixa alta, letter-spacing 0.26em, verde (ou branco a 50% no slide do problema) |
| Corpo | Inter 500 | 28px | line-height 1.5, opacidade 0.82 |
| Subtítulo da capa | Inter 500 | 25px | opacidade 0.78 |
| Rótulos pequenos (balão, legenda de diagrama) | Inter 700 | 13px | caixa alta, letter-spacing 0.22em, opacidade 0.5 |
| Botão do CTA | Space Grotesk 700 | 24px | fundo verde, texto `#16141F`, padding 20px 44px, raio 12px |

`text-wrap: pretty` em parágrafos, frases e headline, pra não sobrar
palavra sozinha na última linha.

### Grid e posições

- Margem lateral do conteúdo: 90px (72px na capa, 80px no CTA).
- Slides internos: texto começa em ~270px do topo. Diagrama, conversa ou
  grade ficam na metade de baixo, a partir de ~750px.
- **Régua** entre título e corpo: 70x4px, raio 2px, verde (ou branco a
  30% no slide do problema).
- **Logo em texto** ("Júlia y Castro", Space Grotesk 700, 20px,
  opacidade 0.85): centralizado no topo na capa; canto inferior direito
  (56px de baixo, 64px da direita) nos slides internos. No CTA entra o
  PNG `logo-claro.png` com 210px, centralizado no topo.

### Estrutura narrativa (7 slides)

1. **Capa** com foto: kicker, título e subtítulo no rodapé, alinhados à
   esquerda
2. **Problema**: o jeito de sempre, em cinza
3. **Virada**: o que eu faço no lugar, com o verde acendendo
4. **Método**: passos numerados
5. **Prova**: o resultado real
6. **Frase de destaque**: uma linha que fecha a ideia, antes do CTA
7. **CTA** com foto: headline, apoio e botão centralizados

Pode ter 7 ou 8 slides se a narrativa pedir. Os slides 2 e 3 funcionam
como antes e depois: mesma altura na tela, primeiro o fluxo cinza,
depois a versão com luz.

### Componentes (classes no HTML de referência)

- **Fluxo** (`.chip` + `.arrow`): caixas com borda branca a 28% e seta
  tracejada com rótulo em cima. Mostra o caminho antigo.
- **Quadros de slide** (`.frame`): miniaturas de slide, as prontas com
  fundo leve e as vazias tracejadas, com legenda "3 de 6" embaixo.
- **Conversa** (`.bubble`): balões com raio 20px e rótulo em cima
  ("VOCÊ", "CLAUDE"). Balão da pessoa: verde a 10% com borda verde a 45%,
  alinhado à direita. Balão da IA: `#16141F` com borda `#2a2636`,
  alinhado à esquerda. Frases curtas, com cara de conversa real.
- **Passos** (`.step` + `.node`): círculo de 64px com borda verde e
  número "01", ligados por uma linha vertical verde em degradê. Texto em
  Inter 600, 33px, e o trecho secundário em 500 com opacidade 0.7.
- **Grade de prova** (`.thumb`): miniaturas reais dos slides, com o
  slide atual em borda verde de 3px e a etiqueta "você está aqui" em
  pílula verde.
- **Nota de rodapé** (`.footnote`): linha fina em cima, Inter 24px,
  opacidade 0.68.

### Regras de texto nos slides

- Sem @ em nenhum slide (o perfil já aparece no post).
- Sem contagem de slides ("1/7").
- Frase de destaque sem aspas.

---

## O que NUNCA fazer

- Não usar amarelo (`#F2C94C`) — testado e descartado, ver seção Cores
- Não usar fundo claro como padrão — a marca é dark-first
- Não adicionar ilustração, ícone decorativo ou elemento gráfico solto —
  a identidade é só tipografia + cor + espaço. Grão, luz difusa e
  diagramas que explicam o conteúdo (fluxo, conversa, passos, prova)
  estão liberados, ver "Padrão de referência: carrossel v2"
- Não usar verde-limão no slide que mostra o problema ou o jeito antigo.
  O verde marca a virada
- Não usar travessão (—) como conector de frase em nenhuma peça de texto
- Não usar frases genéricas de marketing ("sem enrolação", "direto ao
  ponto") — preferir algo concreto sobre o que a peça entrega

---

## Logo

- **Arquivo:** `identidade/logo-escuro.png` (texto escuro, pra fundo claro)
- **Versão pra fundo escuro:** `identidade/logo-claro.png` (texto claro,
  pra fundo escuro. Uso padrão, já que a marca é dark-first)
- **Onde usar:** slide final do carrossel (CTA), header de propostas,
  slides de apresentação
- **Tamanho sugerido:** largura entre 120-200px nos HTMLs (210px no CTA
  do carrossel v2)
- **Nos outros slides:** o nome vai como texto no HTML (Space Grotesk
  700), não como PNG. Posições em "Padrão de referência: carrossel v2".
  O PNG tem só 462px de largura: em peça grande (banner, capa), escrever
  o nome em HTML pra não perder nitidez
- **Tipografia:** Space Grotesk 700, sem símbolo nem ilustração

---

## Padrão 2 — carrossel com foto conceitual (sob demanda)

Padrão opcional, usado só quando explicitamente solicitado (não é o
padrão automático da skill `/carrossel`). Testado e aprovado em
2026-09-14 no carrossel "Como eu crio carrossel com IA (sem app)"
(`marketing/conteudo/carrossel-carrossel-com-ia-2026-09-14/`).

- **Referência de estilo:** fotografia editorial de moda, luz de
  estúdio, pose controlada, colidida com um elemento surreal literal
  que materializa a metáfora do texto do slide (inspirado na linha
  visual da ELLOS, projeto anterior de Júlia). Sempre fotorrealista,
  nunca ilustração ou render 3D estilizado — não conflita com a regra
  de "sem ilustração/ícone decorativo" acima, que trata de elementos
  gráficos soltos, não de fotografia conceitual
- **Distribuição:** imagem só na capa e no slide de CTA final. Slides
  internos ficam texto puro — não repetir imagem em todo slide
- **Quando usar:** quando pedido, ou quando a alternância de capas da
  grade pede foto (regra em `marketing/calendario-instagram.md`: escuro
  sólido, cor sólida e foto, sem repetir o modo do post anterior)
- **Geração:** prompts em inglês, gerados slide a slide a partir da
  metáfora do texto, rodados no Gemini (ver exemplo em
  `marketing/conteudo/carrossel-carrossel-com-ia-2026-09-14/prompts-imagens-gemini.md`).
  O verde-limão aparece dentro da foto como o elemento surreal (o cavalo
  verde da capa, a porta verde do CTA), e o resto da cena fica escuro
- **Aplicação no HTML (v2, atual):** a foto ocupa o slide inteiro e a
  sombra fica só embaixo, onde está o texto, pra foto respirar em cima:
  - Capa: `linear-gradient(180deg, rgba(10,9,7,0) 0%, rgba(10,9,7,0) 54%,
    rgba(10,9,7,0.5) 73%, rgba(10,9,7,0.88) 100%)`, com máscara na foto
    fundindo a base no fundo `#14120d`. Texto no rodapé, alinhado à
    esquerda
  - CTA: `linear-gradient(180deg, rgba(22,20,31,0) 0%, rgba(22,20,31,0)
    58%, rgba(22,20,31,0.78) 76%, rgba(22,20,31,0.96) 90%)`. Texto e
    botão centralizados no rodapé
  - O overlay antigo da v1, escurecendo a foto inteira, saiu

---

## Template de thumbnail

- **Arquivo:** `identidade/thumbnail-template.html` (1280x720, padrão YouTube)
- **Layout:** kicker + título no canto superior esquerdo, recorte de rosto
  embaixo à esquerda, print de tela à direita, logo discreto no canto
  inferior direito
- **Uso:** duplicar o HTML por vídeo, trocar kicker/título e as duas
  imagens (rosto e print), renderizar com Playwright em 1280x720
- **Pendente (antes de 27/09):** alinhar ao padrão v2. O título de 46px
  fica pequeno no celular, os textos aprovados das thumbnails são frases
  curtas em caixa alta ("SEM CANVA, SEM DESIGNER"), falta o grão e o
  espaço do print ainda cita "skill /carrossel"

---

## Observações adicionais
