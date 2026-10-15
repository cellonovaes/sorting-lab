# Design

## Context

Repositório vazio (só git + OpenSpec). Ver `proposal.md` para motivação. As quatro capabilities definem o comportamento observável; aqui cabem as escolhas técnicas já grelhadas.

## Goals / Non-Goals

**Goals:**

- Um único motor (`sort_sequence`) usado por API e CLI.
- Algoritmos isolados, registrados por id, fáceis de estender.
- FastAPI serve JSON, `/docs` e estáticos da UI.
- Testes pytest no mesmo grupo de cada fatia.

**Non-Goals:**

- Docker, CI, auth, banco, CORS extra, ordem descendente, animação de passos, deploy.

## Decisions

### Pacote `src/sorting_lab` e pyproject.toml

- **Por quê:** layout acordado; script `sorting-lab = sorting_lab.cli:main`.
- **Alternativa:** pasta plana sem pacote — piora imports de testes e CLI.

### Motor: registry + arquivos por algoritmo

- Cada algoritmo devolve `(sorted_list, comparisons, swaps | None)`.
- `engine` valida inteiros e n ≤ 10_000, cronometra, não muta a entrada.
- QuickSort: pivô mediana de três (entrada ordenada com n=10_000 não degenera).
- Merge/Tim podem devolver `swaps=None`.
- **Alternativa:** um arquivo só — dificulta testes e extensão.

### API FastAPI + Pydantic

- Rotas em `api/routes.py`, schemas em `api/schemas.py`, app em `main.py`.
- Validação 422 via Pydantic + checagem de `method`.
- Estáticos montados em `/` a partir de `sorting_lab/web/`.
- **Alternativa:** Jinja server-rendered — a UI precisa chamar `POST /sort` como a spec descreve; JS estático cobre isso sem template.

### CLI argparse

- Sequência: string `"5 3 1"`, ints soltos, ou stdin.
- Tabela texto no stdout; erros stderr + exit ≠ 0.
- **Alternativa:** Click — argparse basta e evita dependência extra.

### UI vanilla

- `index.html`, `styles.css`, `app.js` em português.
- Generate só preenche o campo (`crypto`/`Math.random` no cliente).
- **Alternativa:** React — fora do MVP.

### Testes

- `TestClient` para API; `subprocess` ou `CliRunner` interno para CLI; unidade por algoritmo + imutabilidade.
- Sem job de CI.

## Risks / Trade-offs

- [O(n²) com n=10_000] → teto documentado; UI avisa; QuickSort protegido pela mediana de três.
- [Métricas não comparáveis entre linguagens] → aceitável: o laboratório compara implementações deste repo.
- [UI e API desalinhadas] → ids e payload únicos no registry; testes de API como contrato.

## Migration Plan

Greenfield. Não há dados nem versão anterior a migrar. Rollback = não publicar o pacote.

## Open Questions

Nenhuma que altere specs, abordagem ou tasks.
