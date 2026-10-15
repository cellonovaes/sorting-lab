# Spec Delta

## ADDED Requirements

### Requirement: Enriched comparison table
Quando o método escolhido é `all`, a UI SHALL exibir na tabela de resultados as colunas Estável e Complexidade (médio), preenchidas a partir de `GET /methods`.

#### Scenario: All methods show educational columns
- **WHEN** o usuário ordena com todos os métodos e a API responde 200
- **THEN** a tabela inclui colunas de estabilidade e complexidade média além de tempo, comparações e trocas

### Requirement: Single method educational blurb
Quando um único método é selecionado e a ordenação sucede, a UI SHALL mostrar o blurb educacional em português desse método (vindo de `GET /methods`).

#### Scenario: Blurb after single sort
- **WHEN** o usuário ordena com um método individual e a API responde 200
- **THEN** a página exibe o blurb correspondente a esse método

### Requirement: Large-N quadratic warning
A UI SHALL mostrar um aviso não bloqueante em português quando N ≥ 1_000 e o método escolhido é `bubble`, `selection`, `insertion` ou `all`. O aviso SHALL NOT impedir o `POST /sort`.

#### Scenario: Warn on large N with all
- **WHEN** a sequência tem pelo menos 1_000 inteiros e o método é `all`
- **THEN** a UI exibe um aviso sobre algoritmos O(n²) e ainda assim permite ordenar

#### Scenario: No warn on small N
- **WHEN** a sequência tem menos de 1_000 inteiros
- **THEN** a UI não exibe o aviso de N grande por causa do tamanho
