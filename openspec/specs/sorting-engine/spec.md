# sorting-engine Specification

## Purpose
Ordena sequências de inteiros com algoritmos clássicos, valida a entrada e devolve a lista crescente com métricas comparáveis.

## Requirements

### Requirement: Supported algorithms
O sistema SHALL oferecer os métodos `bubble`, `selection`, `insertion`, `merge`, `quick`, `heap` e `tim`, além de `all` para executar os sete na mesma sequência.

#### Scenario: Known method identifiers
- **WHEN** um cliente lista os métodos disponíveis
- **THEN** os ids são exatamente `bubble`, `selection`, `insertion`, `merge`, `quick`, `heap` e `tim`

#### Scenario: Compare all
- **WHEN** a ordenação é pedida com método `all`
- **THEN** o sistema devolve sete resultados, um por algoritmo, todos com a mesma lista ordenada

### Requirement: Input validation
O sistema SHALL aceitar apenas sequências de inteiros com no máximo 10_000 elementos. Lista vazia é válida. Valores não inteiros e tamanho acima do teto SHALL ser rejeitados.

#### Scenario: Empty sequence
- **WHEN** a sequência é `[]`
- **THEN** o resultado ordenado é `[]`

#### Scenario: Negatives zeros and duplicates
- **WHEN** a sequência contém negativos, zero e repetidos
- **THEN** o resultado é a sequência em ordem crescente estável quanto aos valores (iguais permanecem válidos no resultado)

#### Scenario: Non-integer rejected
- **WHEN** a sequência contém um valor que não é inteiro
- **THEN** a ordenação falha com erro de validação

#### Scenario: Oversize rejected
- **WHEN** a sequência tem mais de 10_000 elementos
- **THEN** a ordenação falha com erro de validação

### Requirement: Sort copy ascending
O sistema SHALL devolver uma nova lista em ordem crescente e SHALL NOT mutar a sequência original.

#### Scenario: Input unchanged
- **WHEN** uma sequência `[3, 1, 2]` é ordenada
- **THEN** a lista original permanece `[3, 1, 2]` e o resultado é `[1, 2, 3]`

#### Scenario: Single element
- **WHEN** a sequência é `[7]`
- **THEN** o resultado é `[7]`

### Requirement: Metrics
Cada execução SHALL informar `time_ms`, `comparisons` e `swaps`. Quando o algoritmo não contar trocas, `swaps` SHALL ser nulo.

#### Scenario: Metrics present
- **WHEN** um método individual conclui com sucesso
- **THEN** o resultado inclui tempo em milissegundos, número de comparações e swaps ou nulo
