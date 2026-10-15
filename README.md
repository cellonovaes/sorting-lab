# Sorting Lab

Laboratório educacional para ordenar sequências de inteiros com sete algoritmos clássicos, comparar métricas (tempo, comparações, trocas) e metadados de ensino (complexidade típica, estabilidade, blurb), usando **API**, **CLI** e **interface web** sobre o mesmo motor.

## Pré-requisitos

- Python 3.11+
- `pip`

## Instalação

O comando `uvicorn sorting_lab.main:app` (e o CLI `sorting-lab`) só funcionam **depois** de instalar o pacote em modo editável. Sem isso aparece `ModuleNotFoundError: No module named 'sorting_lab'`.

```bash
cd sorting-lab
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Confirme:

```bash
python -c "import sorting_lab; print('ok')"
```

## Interface web + API

Com o venv ativo:

```bash
uvicorn sorting_lab.main:app --reload --host 127.0.0.1 --port 8000
```

Alternativa sem instalar (só para teste rápido):

```bash
PYTHONPATH=src uvicorn sorting_lab.main:app --reload --host 127.0.0.1 --port 8000
```

- UI: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Endpoints

| Método | Caminho | Descrição |
|--------|---------|-----------|
| `GET` | `/health` | `{ "status": "ok" }` |
| `GET` | `/methods` | Lista ids, nomes e metadados educacionais (complexidade, estabilidade, blurb) |
| `POST` | `/sort` | `{ "sequence": [int], "method": "<id>" \| "all" }` |

### UI educacional

- Modo **Todos**: tabela com tempo, comparações, trocas, **Estável** e **Complexidade (médio)** (valores teóricos típicos, não derivados do `time_ms`).
- Modo **um método**: mostra o **blurb** em português do algoritmo.
- Com **N ≥ 1.000** e método `bubble` / `selection` / `insertion` / `all`, a UI exibe um **aviso não bloqueante** sobre O(n²).

## CLI

```bash
sorting-lab "5 3 8 1"
sorting-lab "5 3 8 1" --method merge
sorting-lab --method all 5 3 8 1
echo "5 3 1" | sorting-lab
sorting-lab --list-methods
```

`--list-methods` imprime nome, complexidade média teórica, estabilidade e blurb de cada algoritmo, sem exigir sequência.

## Algoritmos

`bubble`, `selection`, `insertion`, `merge`, `quick`, `heap`, `tim` — use `all` para executar os sete na mesma entrada.

As strings de complexidade são **classes teóricas clássicas** (best / average / worst). O laboratório compara implementações deste repositório; um único `time_ms` não “prova” Big-O.

## Regras de entrada

- Apenas inteiros (negativos, zero e duplicatas ok)
- Lista vazia permitida
- Máximo **10.000** elementos
- Ordem **crescente**; a entrada original não é mutada

## Testes

Com o venv ativo (após `pip install -e ".[dev]"`):

```bash
pytest tests/ -v
```

## OpenSpec (SDD)

Specs em `openspec/specs/`. Changes arquivados: `openspec/changes/archive/2026-10-14-bootstrap-sorting-lab/` e `openspec/changes/archive/2026-10-15-enrich-educational-comparison/`.
