# Proposal

## Why

Não existe ainda um repositório dedicado a este laboratório: o usuário precisa ordenar inteiros com vários algoritmos, comparar métricas e usar API, CLI e página web no mesmo motor. Os sandboxes anteriores (`openspec-learning`, `teste-tokens-kiro`) não devem ser estendidos.

## What Changes

- Criar o projeto `sorting-lab` com pacote Python, testes e README em português.
- Introduzir um motor de ordenação com sete algoritmos, registro plugável, métricas e validação da entrada.
- Expor o motor via FastAPI (`/health`, `/methods`, `POST /sort`) e Swagger em `/docs`.
- Expor o mesmo motor via CLI `sorting-lab`.
- Servir uma UI estática (HTML/CSS/JS) na mesma origem, com colar, gerar aleatório e comparar um ou todos os métodos.

## Capabilities

### New Capabilities

- `sorting-engine`: ordena sequências de inteiros com os sete algoritmos, valida entrada e devolve métricas.
- `sorting-http-api`: contrato HTTP JSON e documentação OpenAPI.
- `sorting-cli`: interface de linha de comando sobre o mesmo motor.
- `sorting-web-ui`: página web local para informar a sequência, escolher o método e ver resultados.

### Modified Capabilities

- (nenhuma — projeto novo, `openspec/specs/` vazio)

## Impact

- Código novo em `src/sorting_lab/` e `tests/`; `pyproject.toml` com fastapi, uvicorn, pytest, httpx.
- Sem Docker, CI, autenticação, persistência, CORS extra, ordem descendente ou deploy.
- CLI e API compartilham o mesmo registry; não há segundo conjunto de algoritmos.
