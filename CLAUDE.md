# Júlia y Castro — Y OS

> Molde do CLAUDE.md aplicado a **criador solo** — uma pessoa, uma marca,
> audiência como ativo principal. O sistema gira em torno do que você
> produz e publica.

## O que é esse workspace

Operação da Y OS, consultoria de IA de Júlia y Castro. Aqui ela estrutura
a empresa, produz conteúdo, define posicionamento e organiza a aquisição
de clientes.

**Estrutura de pastas:**
- `_memoria/` — quem eu sou, como falo, o que tá em foco
- `identidade/` — cores, fontes, logo, padrão visual
- `marketing/` — conteúdo, SEO, campanhas (saída das skills)
- `saidas/` — análises, emails, documentos pontuais
- `produtos/` — meus produtos próprios (cursos, ebooks, ofertas)
- `audiencia/` — listas, dados, contatos da minha base
- `dados/` — arquivos a analisar (CSV, PDF, planilha)
- `scripts/` — utilitários (gerar imagem, postar, render)
- `tarefas.md` — o que tá em jogo agora

## Quem sou

Sou Júlia y Castro, 25 anos. Estou estruturando a Y OS, uma consultoria
de IA, do zero — ainda na fase de abertura da empresa.

## O que produzo

- Conteúdo de prospecção e presença (a definir formato conforme a marca evolui)
- Copy para mensagens de prospecção de clientes
- Consultoria de IA aplicada a marketing e operação, nas mesmas frentes do MazyOS:
  - Conteúdo e SEO (carrosséis, posts, blog, SEO/GEO, avaliações do Google)
  - Anúncios pagos (Google Ads, relatórios de performance)
  - Produção e operação (análise de dados, automação de rotinas, emails)

## Minha audiência

Perfil de cliente ideal ainda não definido — a construir junto ao longo
do projeto, sem persona genérica por enquanto.

## Tom de voz

Ainda não definido — sem exemplo de escrita real disponível ainda. Calibrar
conforme Júlia for produzindo conteúdo real.

Evitar: jargão de guru (ex. "alavancar", "sinergia"); emoji em email formal.

## Posicionamento

Em construção.

## Regras do sistema

- Conteúdo novo salvar em `marketing/conteudo/<tipo>-<tema>-<data>/`
- Cada lançamento de produto cria pasta em `produtos/<nome>/`
- Prioridade atual: estruturação da empresa e aquisição de clientes (ver `_memoria/estrategia.md`)

## Ferramentas conectadas

- [ ] Notion
- [ ] Canva
- [ ] Google Calendar
- [ ] Meta Ads
- [ ] Google Ads

*(Marcar conforme for instalando os MCPs)*

---

# Regras de operação do MazyOS

Aqui ficam as regras de operação do MazyOS — como o Claude lê o contexto,
aprende com correções, mantém tudo atualizado e cria skills novas conforme
a operação evolui.

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem
e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, prazos

Usar essas informações como base pra qualquer resposta ou decisão. Ao
sugerir prioridades, formatos ou abordagens, considerar o foco atual
descrito em `estrategia.md`.

Pra qualquer tarefa visual (carrossel, post, landing page), consultar
`identidade/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas
usar o contexto naturalmente.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante
em `.claude/skills/`. Se encontrar, seguir as instruções da skill. Se
não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o
usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o
padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma
instrução que parece permanente (frases como "na verdade é assim", "não
faça mais isso", "prefiro assim", "sempre que...", "evita...", "da
próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (clientes, serviços, mercado) → `_memoria/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato, o que evitar) → `_memoria/preferencias.md`
- **Sobre prioridades e foco** (projetos, metas, prazos) → `_memoria/estrategia.md`
- **Regra de comportamento nessa pasta** → próprio `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro.
Confirmar mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na
verdade o arquivo se chama X"). Só perguntar quando a informação tiver
valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (cliente novo, skill
nova, mudança de foco, processo novo, ferramenta instalada, estrutura
alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

Se sim, identificar o que atualizar:

- **Cliente, serviço, ferramenta, equipe** → `_memoria/empresa.md`
- **Mudança de prioridade ou foco** → `_memoria/estrategia.md`
- **Tom ou estilo** → `_memoria/preferencias.md`
- **Pasta, regra de organização, skill criada** → `CLAUDE.md`
- **Visual (cores, fontes, logo)** → `identidade/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo
inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais sem impacto no contexto (escrever um email avulso, criar um post)
- Perguntas simples ou conversas sem ação
- Mudanças já salvas pelo bloco "Aprender com correções"

**Dica:** rode `/atualizar` pra uma varredura completa quando houver dúvida.

---

## Criação de skills

Quando o usuário pedir skill nova:

1. Verificar se existe template relevante em `templates/skills/`. Se
   existir, usar como base e adaptar pro contexto
2. Perguntar se é específica desse projeto ou útil em qualquer:
   - Específica → `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Universal → `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` pra calibrar
   o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, exemplos),
   criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code
</content>
