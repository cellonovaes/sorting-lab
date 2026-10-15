# Sorting Lab

Laboratório educacional para ordenar sequências de inteiros com sete algoritmos clássicos, comparar métricas (tempo, comparações, trocas) e usar **API**, **CLI** e **interface web** sobre o mesmo motor.

## Pré-requisitos

- Python 3.11+
- `pip`

## Instalação

```bash
cd sorting-lab
pip install -e ".[dev]"
```

## Interface web + API

```bash
uvicorn sorting_lab.main:app --reload --host 127.0.0.1 --port 8000
```

- UI: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Endpoints

| Método | Caminho | Descrição |
|--------|---------|-----------|
| `GET` | `/health` | `{ "status": "ok" }` |
| `GET` | `/methods` | Lista ids e nomes dos algoritmos |
| `POST` | `/sort` | `{ "sequence": [int], "method": "<id>" \| "all" }` |

## CLI

```bash
sorting-lab "5 3 8 1"
sorting-lab "5 3 8 1" --method merge
sorting-lab --method all 5 3 8 1
echo "5 3 1" | sorting-lab
```

## Algoritmos

`bubble`, `selection`, `insertion`, `merge`, `quick`, `heap`, `tim` — use `all` para executar os sete na mesma entrada.

## Regras de entrada

- Apenas inteiros (negativos, zero e duplicatas ok)
- Lista vazia permitida
- Máximo **10.000** elementos
- Ordem **crescente**; a entrada original não é mutada

## Testes

```bash
pytest tests/ -v
```

## OpenSpec (SDD)

Planejamento em `openspec/changes/bootstrap-sorting-lab/`. Após validar a implementação, arquive a change com `openspec archive bootstrap-sorting-lab`.
