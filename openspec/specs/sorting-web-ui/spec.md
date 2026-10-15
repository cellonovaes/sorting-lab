# sorting-web-ui Specification

## Purpose
Oferece uma página web local, na mesma origem da API, para colar ou gerar inteiros, escolher o algoritmo e ver resultado e métricas.

## Requirements

### Requirement: Static UI same origin
O sistema SHALL servir a interface HTML/CSS/JS no mesmo host da API, em português, sem SPA de framework.

#### Scenario: Open root
- **WHEN** o usuário abre `http://127.0.0.1:8000/` com o servidor no ar
- **THEN** a página de ordenação é exibida

### Requirement: Sequence input
A UI SHALL permitir colar uma sequência de inteiros e gerar N aleatórios. N default SHALL ser 20 no intervalo inclusivo [-100, 100]. N SHALL estar entre 1 e 10_000.

#### Scenario: Generate fills field
- **WHEN** o usuário pede gerar com os defaults
- **THEN** o campo de sequência é preenchido com 20 inteiros em [-100, 100] e nenhum `POST /sort` é enviado só por gerar

#### Scenario: Invalid N blocks generate
- **WHEN** N está fora de 1–10_000
- **THEN** a UI não chama a API de ordenação para gerar e informa o problema

### Requirement: Run one or all
A UI SHALL permitir escolher um dos sete métodos ou todos, chamar `POST /sort`, e mostrar a lista ordenada mais tempo, comparações e trocas (hífen quando swaps é nulo).

#### Scenario: Single method display
- **WHEN** o usuário ordena com um método e a API responde 200
- **THEN** a página mostra a lista ordenada e as métricas desse método

#### Scenario: All methods display
- **WHEN** o usuário ordena com todos e a API responde 200
- **THEN** a página mostra uma tabela com os sete métodos e a lista ordenada

#### Scenario: Null swaps
- **WHEN** um resultado traz `swaps` nulo
- **THEN** a UI exibe `-` na coluna de trocas

### Requirement: UI error display
A UI SHALL mostrar o erro quando a API responde 422 ou a entrada local é inválida.

#### Scenario: API 422
- **WHEN** `POST /sort` retorna 422
- **THEN** a página mostra uma mensagem de erro compreensível em português

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
