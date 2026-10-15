import time

from sorting_lab.sorting.registry import METHOD_IDS, SORTERS
from sorting_lab.sorting.types import MAX_SEQUENCE_LENGTH, SortRunResult


class SequenceValidationError(ValueError):
    """Entrada inválida para ordenação."""


def validate_sequence(sequence: list) -> list[int]:
    if len(sequence) > MAX_SEQUENCE_LENGTH:
        raise SequenceValidationError(
            f"A sequência excede o limite de {MAX_SEQUENCE_LENGTH} elementos."
        )
    validated: list[int] = []
    for item in sequence:
        if isinstance(item, bool) or not isinstance(item, int):
            raise SequenceValidationError("A sequência deve conter apenas inteiros.")
        validated.append(item)
    return validated


def _run_one(method_id: str, sequence: list[int]) -> SortRunResult:
    sorter = SORTERS[method_id]
    start = time.perf_counter()
    sorted_data, comparisons, swaps = sorter(sequence)
    elapsed_ms = (time.perf_counter() - start) * 1000
    return SortRunResult(
        method=method_id,
        sorted=sorted_data,
        time_ms=elapsed_ms,
        comparisons=comparisons,
        swaps=swaps,
    )


def sort_sequence(sequence: list, method: str) -> list[SortRunResult]:
    validated = validate_sequence(sequence)
    if method == "all":
        return [_run_one(method_id, validated) for method_id in METHOD_IDS]
    if method not in SORTERS:
        raise SequenceValidationError(f"Método desconhecido: {method}")
    return [_run_one(method, validated)]
