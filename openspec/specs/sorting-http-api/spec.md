# sorting-http-api Specification

## Purpose
Expõe o motor de ordenação por HTTP JSON, com saúde, listagem de métodos, execução e documentação OpenAPI automática.

## Requirements

### Requirement: Health endpoint
O sistema SHALL responder `GET /health` com `{ "status": "ok" }` quando o serviço está no ar.

#### Scenario: Healthy
- **WHEN** um cliente chama `GET /health`
- **THEN** a resposta é 200 e o corpo contém `status` igual a `ok`

### Requirement: Methods endpoint
O sistema SHALL responder `GET /methods` com `{ "methods": [ { "id", "name", "complexity_best", "complexity_average", "complexity_worst", "stable", "blurb" }, ... ] }` cobrindo os sete algoritmos. Os campos de complexidade e blurb SHALL refletir os metadados educacionais do motor; `stable` SHALL ser booleano.

#### Scenario: List methods
- **WHEN** um cliente chama `GET /methods`
- **THEN** a resposta é 200 e inclui id e nome de cada um dos sete algoritmos

#### Scenario: Educational fields present
- **WHEN** um cliente chama `GET /methods`
- **THEN** cada item inclui `complexity_best`, `complexity_average`, `complexity_worst`, `stable` e `blurb` preenchidos

### Requirement: Sort endpoint
O sistema SHALL aceitar `POST /sort` com corpo `{ "sequence": [int], "method": "<id>" | "all" }` e devolver `{ "results": [ ... ] }`. Cada item SHALL conter `method`, `sorted`, `time_ms`, `comparisons` e `swaps`.

#### Scenario: Single method
- **WHEN** o cliente envia `method` `merge` e uma sequência válida
- **THEN** a resposta é 200 e `results` tem exatamente um item com `method` `merge` e a lista ordenada

#### Scenario: All methods
- **WHEN** o cliente envia `method` `all` e uma sequência válida
- **THEN** a resposta é 200 e `results` tem sete itens

### Requirement: Sort validation errors
O sistema SHALL responder 422 quando `method` é desconhecido, a sequência contém não-inteiros, ou n > 10_000.

#### Scenario: Unknown method
- **WHEN** `POST /sort` usa um `method` que não é um dos ids nem `all`
- **THEN** a resposta é 422

#### Scenario: Invalid items
- **WHEN** `sequence` contém um não-inteiro
- **THEN** a resposta é 422

#### Scenario: Sequence too long
- **WHEN** `sequence` tem mais de 10_000 elementos
- **THEN** a resposta é 422

### Requirement: OpenAPI docs
O sistema SHALL publicar a documentação interativa OpenAPI em `/docs`.

#### Scenario: Swagger available
- **WHEN** um cliente abre `/docs` com o servidor no ar
- **THEN** a página de documentação da API é servida
