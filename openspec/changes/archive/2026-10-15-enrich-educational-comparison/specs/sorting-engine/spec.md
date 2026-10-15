# Spec Delta

## ADDED Requirements

### Requirement: Educational method metadata
O sistema SHALL expor, para cada um dos sete ids de método, metadados educacionais estáticos: complexidade típica teórica (best, average, worst como strings), estabilidade booleana e um blurb curto em português. Esses valores SHALL NOT ser derivados de uma medição `time_ms`.

#### Scenario: Metadata for every method id
- **WHEN** um cliente consulta os metadados dos métodos
- **THEN** cada id entre `bubble`, `selection`, `insertion`, `merge`, `quick`, `heap` e `tim` tem complexidade best/average/worst, `stable` e blurb não vazio em português

#### Scenario: Quadratic family marked for warnings
- **WHEN** o cliente consulta metadados de `bubble`, `selection` ou `insertion`
- **THEN** a complexidade média indica classe O(n²) (string contendo `n²` ou `n^2`)
