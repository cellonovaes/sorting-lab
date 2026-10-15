# Design

## Context

MVP arquivado com registry de ids → funções. `GET /methods` devolve só `id`/`name`. UI monta labels locais. Ver `proposal.md` para motivação.

## Goals / Non-Goals

**Goals:**

- Uma única fonte de metadados educacionais no registry, consumida por API, CLI e UI.
- Complexidade explícita como strings teóricas (não calculadas de `time_ms`).
- Aviso de N grande só na UI (cliente conhece N antes do POST).

**Non-Goals:**

- Inferir Big-O a partir de corridas; alterar contadores de swaps; novos algoritmos; warmup de timing.

## Decisions

### Dataclass `MethodMeta` + mapa no registry

- Campos: `id`, `name`, `complexity_best`, `complexity_average`, `complexity_worst`, `stable`, `blurb`.
- `METHOD_NAMES` / `SORTERS` / `METHOD_IDS` continuam derivados do mesmo mapa (ou `METHOD_NAMES` passa a ler o meta) para não divergir.
- **Alternativa:** JSON estático na pasta `web/` — quebraria a regra de fonte única com a API/CLI.

### Strings clássicas de complexidade

| id | best | average | worst | stable |
|----|------|---------|-------|--------|
| bubble | O(n) | O(n²) | O(n²) | true |
| selection | O(n²) | O(n²) | O(n²) | false |
| insertion | O(n) | O(n²) | O(n²) | true |
| merge | O(n log n) | O(n log n) | O(n log n) | true |
| quick | O(n log n) | O(n log n) | O(n²) | false |
| heap | O(n log n) | O(n log n) | O(n log n) | false |
| tim | O(n) | O(n log n) | O(n log n) | true |

Blurbs em PT, 1–2 frases, mencionando ideia central (ex.: bubble troca adjacentes; merge divide-e-conquista).

### API: estender `MethodInfo`

Campos novos obrigatórios no schema Pydantic. Clientes antigos que só leem `id`/`name` seguem válidos.

### CLI: `--list-methods`

Flag booleana; se presente, imprime lista formatada e retorna 0 sem chamar `sort_sequence`. Mutuamente prioritária sobre ordenação.

### UI: cache de `/methods` + colunas dinâmicas

- Guardar o array de métodos ao carregar.
- Cabeçalho da tabela: no modo `all` inclui Estável e Complexidade (médio); no modo single, colunas métricas atuais + bloco de blurb.
- Aviso: função que checa `sequence.length >= 1000` e método ∈ {bubble, selection, insertion, all}; texto em `#message` com estilo não-erro (muted/warning) **antes** ou **junto** do POST, sem `return` precoce.

### Testes

- API: assertar campos educacionais em `/methods`.
- CLI: `sorting-lab --list-methods` exit 0 + conteúdo.
- Registry/unidade: sete metas com average contendo `n²`/`n^2` para a família quadrática.
- UI: verificação manual + smoke de HTML (colunas/elementos presentes no markup onde couber).

## Risks / Trade-offs

- [TimSort “O(n)” no melhor caso é simplificação didática] → aceitável; blurb pode notar que é híbrido.
- [Aviso só no cliente] → API/CLI não avisam; documentado no README.
- [Tabela mais larga] → `overflow-x: auto` já existe.

## Migration Plan

Greenfield sobre o MVP. Rollback = reverter o change. Sem migração de dados.

## Open Questions

Nenhuma que altere specs, abordagem ou tasks.
