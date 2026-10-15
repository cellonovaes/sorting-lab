# Proposal

## Why

O MVP já ordena e compara métricas, mas o aprendiz não vê **por que** os algoritmos diferem: não há complexidade teórica, estabilidade nem texto curto de ensino. A UI também não avisa quando N grande torna O(n²) doloroso — risco já notado no design do bootstrap.

## What Changes

- Acrescentar metadados educacionais por algoritmo no registry (complexidade típica best/avg/worst, estabilidade, blurb PT).
- Enriquecer `GET /methods` para expor esses campos (fonte única para UI e CLI).
- Na UI: colunas Estável e Complexidade (médio) no modo `all`; blurb no modo de um método; aviso não bloqueante quando N ≥ 1_000 e o método é quadrático ou `all`.
- No CLI: caminho de listagem/explicação (`--list-methods`) com os mesmos metadados.
- Atualizar o README (campos novos + clarificações de instalação já pendentes).

**Fora de escopo:** Docker, CI, auth, banco, deploy, ordem descendente, animação de passos, novos algoritmos, React/SPA, warmup/múltiplas medições de tempo.

## Capabilities

### New Capabilities

- (nenhuma)

### Modified Capabilities

- `sorting-engine`: metadados educacionais estáticos por id de método no registry.
- `sorting-http-api`: `GET /methods` passa a incluir complexidade, estabilidade e blurb.
- `sorting-cli`: flag/comando para listar métodos com metadados educacionais.
- `sorting-web-ui`: tabela enriquecida, blurb no método único, aviso de N grande.

## Impact

- Código: `sorting/registry.py` (e possivelmente `types.py`), `api/schemas.py`, `api/routes.py`, `cli.py`, `web/{index.html,app.js,styles.css}`, testes API/CLI/registry, `README.md`.
- Contrato JSON de `/methods` ganha campos novos (compatível para clientes que ignoram campos extras).
- Sem novas dependências de runtime.
