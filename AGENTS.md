# Regras para o agente — formação ICC System Design

Este repositório guarda o estado da formação ICC, conduzida com a skill `ai-tutor`. O estado canônico é `.ai-tutor/state.json`; `session-log.md` é gerado a partir dele.

## Captura no Segundo Cérebro (decisão do aluno, 2026-11-11)

Ao **fechar ou interromper cada sessão de estudo**, gravar uma nota de sessão no cofre, na mesma virada do fechamento, sem esperar pedido.

- **Cofre:** `C:\Users\lucka\Documents\Segundo Cérebro`. Antes de gravar, ler o `CLAUDE.md` e o `MAPA.md` da raiz do cofre: eles mandam no esquema.
- **Pasta e nome:** `70 - Sessões Claude\AAAA-MM-DD ICC - <assunto curto>.md`, seguindo o template `00 - Sistema/Templates/Sessão Claude.md`.
- **Frontmatter:** `tipo: sessao`, `status: ativo`, `criado`, `dominio: trabalho`, `area: "[[ICC System Design]]"`, `origem` (este repositório), `session_id` canônico e `tags` (`icc`, `ferrovia` e o tópico).
- **Conteúdo factual:** como o aluno raciocinou, as dúvidas, os erros e como foram resolvidos, o que ficou pendente e links para a lição e para os arquivos do projeto Linha Aurora.
- **Projeção, não evidência:** a nota não altera `mastery` nem substitui o `session-log.md`.
- **Estado do cofre, na mesma virada:**
  - `hot.md`: a linha do ICC na seção Trabalho (lição ativa e próximo passo);
  - `pendencias.md`: na seção Trabalho, riscar o que foi feito e acrescentar os próximos passos, cada um com `(desde AAAA-MM-DD)`;
  - `20 - Áreas/Trabalho/ICC System Design.md`: atualizar a seção "Estado" quando uma lição ou fase fechar.
- **Notas permanentes:** na seção "Candidatas a nota permanente", o tutor só lista ideias (uma frase e a sessão de origem). Quem escreve é o aluno.
- **Decisões** do aluno sobre a formação entram em `80 - Decisões/AAAA-MM.md` do cofre.
- **Nada confidencial:** a regra deste repositório vale para o cofre. Documentos internos de empresa, dados de clientes e trechos de normas pagas nunca entram na nota.
