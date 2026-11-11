# Regras para o agente — formação ICC System Design

Este repositório guarda o estado da formação ICC, conduzida com a skill `ai-tutor`. O estado canônico é `.ai-tutor/state.json`; `session-log.md` é gerado a partir dele.

## Captura no Segundo Cérebro (decisão do aluno, 2026-11-11)

Ao **fechar ou interromper cada sessão de estudo**, gravar uma nota de sessão no cofre do aluno, na mesma virada do fechamento, sem esperar pedido.

- **Onde fica o cofre:** o caminho está na skill global `segundo-cerebro`, na máquina do aluno. Se a skill não estiver disponível, pergunte o caminho ao aluno. Este repositório é público e não guarda caminhos locais.
- **Pré-condição, antes de gravar qualquer coisa:** confira que o cofre está atualizado. Ele está atualizado quando `20 - Áreas/Trabalho/ICC System Design.md`, `hot.md` e `pendencias.md` existem e `10 - Projetos/ICC System Design.md` não existe. Se a conferência falhar, não grave nada no cofre: avise o aluno para rodar `git pull` no cofre e só então gravar.
- **Esquema:** ler o `CLAUDE.md` e o `MAPA.md` da raiz do cofre. Eles mandam no esquema e valem sobre esta lista se houver diferença.
- **Pasta e nome:** `70 - Sessões Claude/AAAA-MM-DD ICC - <assunto curto>.md`, seguindo o template `00 - Sistema/Templates/Sessão Claude.md`.
- **Frontmatter:** `tipo: sessao`, `status: ativo`, `criado`, `dominio: trabalho`, `area: "[[ICC System Design]]"`, `origem` (este repositório), `session_id` canônico e `tags` (`icc`, `ferrovia` e o tópico).
- **Conteúdo factual:** como o aluno raciocinou, as dúvidas, os erros e como foram resolvidos, o que ficou pendente e links para a lição e para os arquivos do projeto Linha Aurora.
- **Projeção, não evidência:** a nota não altera `mastery` nem substitui o `session-log.md`.
- **Estado do cofre, na mesma virada:**
  - `hot.md`: a linha do ICC na seção Trabalho (lição ativa e próximo passo);
  - `pendencias.md`: na seção Trabalho, fechar as pendências feitas como manda o `CLAUDE.md` do cofre (marcar `- [x]`) e acrescentar os próximos passos, cada um com `(desde AAAA-MM-DD)`;
  - `20 - Áreas/Trabalho/ICC System Design.md`, seção `## Estado` (o título é fixo e não leva data): a cada sessão, atualizar a próxima sessão, as sessões e a linha `Atualizado em AAAA-MM-DD`; quando uma lição ou fase fechar, atualizar também a fase e o domínio.
- **Notas permanentes:** na seção "Candidatas a nota permanente", o tutor só lista ideias (uma frase e a sessão de origem). Quem escreve é o aluno.
- **Decisões** do aluno sobre a formação entram em `80 - Decisões/AAAA-MM.md` do cofre, no formato que o `CLAUDE.md` do cofre define.

## Confidencialidade

Vale a regra mais restritiva entre este repositório e o `CLAUDE.md` do cofre. Nunca entram na nota de sessão, nem neste repositório:

- documentos internos, normas pagas e dados de clientes;
- informação operacional de empregador ou de fornecedor: ocorrências reais, configurações de equipamentos, nomes de linhas e estações reais e procedimentos internos.

Quando um exemplo do trabalho ajudar o raciocínio, use um exemplo genérico ou a Linha Aurora. Na dúvida, não registre e pergunte ao aluno.
