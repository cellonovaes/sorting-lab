# Tasks

## 1. Scaffold

- [x] 1.1 Criar `pyproject.toml` (Python ≥3.11, fastapi, uvicorn, pytest, httpx, script `sorting-lab`) e estrutura `src/sorting_lab/` + `tests/` e verificar que `pip install -e ".[dev]"` ou extra de teste resolve as deps
- [x] 1.2 Adicionar `__init__.py` nos pacotes e um `main.py` FastAPI vazio que sobe e verificar `GET /health` placeholder ou import `sorting_lab.main:app`

## 2. Motor de ordenação

- [x] 2.1 Implementar os sete algoritmos com cópia, crescente, contadores internos e QuickSort com mediana de três e verificar `tests/test_algorithms.py` (`[]`, `[1]`, ordenado, reverso, duplicatas, negativos, golden, input imutável)
- [x] 2.2 Implementar registry + `sort_sequence` (`all` e ids) com validação n ≤ 10_000 / não-inteiro e verificar `tests/test_registry.py` (sete resultados, `sorted` idêntico)

## 3. API HTTP

- [x] 3.1 Implementar schemas e rotas `GET /health`, `GET /methods`, `POST /sort` e verificar `tests/test_api.py` (feliz, `all`, 422 method/não-inteiro/n>10000)
- [x] 3.2 Montar `/docs` no app e verificar que `/docs` responde 200

## 4. CLI

- [x] 4.1 Implementar `cli.py` (aspas, args, stdin, default `all`, tabela stdout) e verificar `tests/test_cli.py` (`--method merge`, default `all`, stdin vazio = `[]`)
- [x] 4.2 Tratar erros de validação no CLI e verificar exit ≠ 0 + stderr para não-inteiro, n > 10_000 e method desconhecido

## 5. UI web

- [x] 5.1 Servir `web/index.html`, `styles.css`, `app.js` em `/` e verificar que `GET /` devolve HTML em português
- [x] 5.2 Implementar colar, gerar N (default 20, [-100,100], N 1–10000 sem POST), um método ou todos, métricas e `-` para swaps nulo, erro 422 e verificar manualmente em `http://127.0.0.1:8000`

## 6. Integração

- [x] 6.1 Escrever `README.md` em português (CLI, API, UI, testes, `uvicorn` em 127.0.0.1:8000) e verificar que os comandos documentados batem com o código
- [x] 6.2 Rodar `pytest tests/ -v` na raiz e verificar suite verde

## Workflow follow-up

- Arquivar `bootstrap-sorting-lab` com `openspec archive` depois que pytest passar e o usuário confirmar.
- Validar o resultado arquivado (`openspec list --specs`).
