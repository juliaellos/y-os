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

## Elementos-chave

- Bordas: 1px, cor `#2a2636` (mistura de fundo alternativo com um pouco
  de luz). Usar com moderação, preferir espaço em branco a separar com
  linha
- Border-radius dos cards: 12-14px
- Botões: preenchido com verde-limão (`#C6F135`) + texto `#16141F` pro CTA
  principal; contorno roxo (`#5B3FA0`) + texto verde-limão pro secundário
- Sombras: evitar. Se precisar separar camada, usar fundo alternativo
  (`#201D2E`) em vez de sombra

---

## O que NUNCA fazer

- Não usar amarelo (`#F2C94C`) — testado e descartado, ver seção Cores
- Não usar fundo claro como padrão — a marca é dark-first
- Não adicionar ilustração, ícone decorativo ou elemento gráfico solto —
  a identidade é só tipografia + cor + espaço
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
- **Tamanho sugerido:** largura entre 120-200px nos HTMLs
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
- **Geração:** prompts em inglês, gerados slide a slide a partir da
  metáfora do texto, rodados no Gemini (ver exemplo em
  `marketing/conteudo/carrossel-carrossel-com-ia-2026-09-14/prompts-imagens-gemini.md`)
- **Aplicação no HTML:** foto como `background-image` do slide, com
  overlay `linear-gradient(180deg, rgba(22,20,31,0.35) 0%,
  rgba(22,20,31,0.55) 55%, rgba(22,20,31,0.9) 100%)` por cima pra manter
  o texto legível

---

## Template de thumbnail

- **Arquivo:** `identidade/thumbnail-template.html` (1280x720, padrão YouTube)
- **Layout:** kicker + título no canto superior esquerdo, recorte de rosto
  embaixo à esquerda, print de tela à direita, logo discreto no canto
  inferior direito
- **Uso:** duplicar o HTML por vídeo, trocar kicker/título e as duas
  imagens (rosto e print), renderizar com Playwright em 1280x720

---

## Observações adicionais
