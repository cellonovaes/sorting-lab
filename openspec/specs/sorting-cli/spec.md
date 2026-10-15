# sorting-cli Specification

## Purpose
Permite ordenar a mesma sequência de inteiros na linha de comando, reutilizando o motor da API, com tabela de métricas e códigos de saída.

## Requirements

### Requirement: Invoke sort from CLI
O comando `sorting-lab` SHALL aceitar a sequência como string entre aspas, como argumentos numéricos, ou via stdin quando a sequência é omitida. `--method` default SHALL ser `all`. Os ids de método SHALL ser os mesmos da API.

#### Scenario: Quoted sequence one method
- **WHEN** o usuário executa `sorting-lab "5 3 8 1" --method merge`
- **THEN** o comando termina com exit 0 e imprime métricas de merge e a lista ordenada

#### Scenario: Default all
- **WHEN** o usuário executa `sorting-lab "5 3 8 1"` sem `--method`
- **THEN** o comando termina com exit 0 e imprime uma tabela com os sete métodos

#### Scenario: Stdin sequence
- **WHEN** não há sequência nos argumentos e stdin contém `5 3 8 1`
- **THEN** o comando ordena essa sequência

#### Scenario: Empty stdin
- **WHEN** não há sequência nos argumentos e stdin está vazio
- **THEN** o comando trata a entrada como `[]` e termina com exit 0

### Requirement: CLI output format
Em sucesso o CLI SHALL escrever no stdout uma tabela com método, tempo_ms, comparações, trocas e a lista ordenada uma vez.

#### Scenario: Table on stdout
- **WHEN** a ordenação CLI conclui com sucesso
- **THEN** stdout contém as colunas de métricas e a sequência ordenada, e stderr não traz o resultado principal

### Requirement: CLI validation errors
O CLI SHALL escrever a mensagem de erro em stderr e sair com código diferente de 0 quando a entrada não é inteira, n > 10_000, ou o método é desconhecido.

#### Scenario: Non-integer
- **WHEN** a sequência CLI contém um token que não é inteiro
- **THEN** exit ≠ 0 e a mensagem vai para stderr

#### Scenario: Oversize
- **WHEN** a sequência CLI tem mais de 10_000 inteiros
- **THEN** exit ≠ 0 e a mensagem vai para stderr

#### Scenario: Unknown method
- **WHEN** `--method` não é um id conhecido nem `all`
- **THEN** exit ≠ 0 e a mensagem vai para stderr
