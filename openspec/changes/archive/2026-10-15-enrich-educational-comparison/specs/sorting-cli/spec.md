# Spec Delta

## ADDED Requirements

### Requirement: List methods with educational metadata
O CLI SHALL aceitar `--list-methods` para listar os sete algoritmos com nome, complexidade média teórica, estabilidade e blurb em português, sem exigir sequência de entrada. Em sucesso SHALL sair com código 0 e escrever no stdout.

#### Scenario: List methods exits zero
- **WHEN** o usuário executa `sorting-lab --list-methods`
- **THEN** o comando termina com exit 0 e stdout inclui os sete nomes de método e pelo menos um blurb em português

#### Scenario: List methods needs no sequence
- **WHEN** o usuário executa `sorting-lab --list-methods` sem argumentos de sequência
- **THEN** o comando não exige stdin nem inteiros e não falha por sequência vazia
