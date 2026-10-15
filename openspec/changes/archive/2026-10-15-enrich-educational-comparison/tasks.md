# Tasks

## 1. Registry e metadados

- [x] 1.1 Adicionar `MethodMeta` e mapa educacional completo no registry (complexidade, stable, blurb PT) mantendo `SORTERS`/`METHOD_IDS`/`METHOD_NAMES` coerentes e verificar teste de unidade dos sete ids + família O(n²)
- [x] 1.2 Expor helper de listagem dos metadados usado por API/CLI e verificar import estável

## 2. API HTTP

- [x] 2.1 Estender `MethodInfo`/`MethodsResponse` e a rota `GET /methods` com os campos educacionais e verificar `tests/test_api.py` (campos presentes nos sete métodos)

## 3. CLI

- [x] 3.1 Implementar `--list-methods` (stdout com nome, complexidade média, estabilidade, blurb; exit 0 sem sequência) e verificar `tests/test_cli.py`

## 4. UI web

- [x] 4.1 Atualizar `index.html`/`app.js`/`styles.css`: cache de `/methods`, colunas Estável/Complexidade no `all`, blurb no método único, aviso N≥1000 para bubble/selection/insertion/all e verificar smoke HTML + checagem manual em `http://127.0.0.1:8000`

## 5. README e integração

- [x] 5.1 Atualizar README (metadados, `/methods`, aviso, `--list-methods`, clarificações de instalação) e verificar que os comandos documentados batem com o código
- [x] 5.2 Rodar `pytest tests/ -v` na raiz e verificar suite verde

## Workflow follow-up

- Arquivar `enrich-educational-comparison` depois que pytest passar e o usuário confirmar.
- Validar o resultado arquivado (`openspec list --specs`).
