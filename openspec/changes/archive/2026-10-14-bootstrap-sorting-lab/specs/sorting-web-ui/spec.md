# Spec Delta

## Purpose

Oferece uma página web local, na mesma origem da API, para colar ou gerar inteiros, escolher o algoritmo e ver resultado e métricas.

## ADDED Requirements

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
