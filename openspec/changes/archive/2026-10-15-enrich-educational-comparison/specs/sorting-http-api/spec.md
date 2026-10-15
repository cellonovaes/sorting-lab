# Spec Delta

## MODIFIED Requirements

### Requirement: Methods endpoint
O sistema SHALL responder `GET /methods` com `{ "methods": [ { "id", "name", "complexity_best", "complexity_average", "complexity_worst", "stable", "blurb" }, ... ] }` cobrindo os sete algoritmos. Os campos de complexidade e blurb SHALL refletir os metadados educacionais do motor; `stable` SHALL ser booleano.

#### Scenario: List methods
- **WHEN** um cliente chama `GET /methods`
- **THEN** a resposta é 200 e inclui id e nome de cada um dos sete algoritmos

#### Scenario: Educational fields present
- **WHEN** um cliente chama `GET /methods`
- **THEN** cada item inclui `complexity_best`, `complexity_average`, `complexity_worst`, `stable` e `blurb` preenchidos
