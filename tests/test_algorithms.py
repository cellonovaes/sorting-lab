import pytest

from sorting_lab.sorting.registry import SORTERS

GOLDEN = ([5, 3, 8, 1, 9, 2], [1, 2, 3, 5, 8, 9])

CASES = [
    [],
    [1],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [3, 1, 3, 2, 1],
    [-3, 0, 5, -1, 0],
    GOLDEN[0],
]


@pytest.mark.parametrize("method_id", list(SORTERS.keys()))
@pytest.mark.parametrize("sequence", CASES, ids=lambda s: repr(s))
def test_algorithm_sorts(method_id: str, sequence: list[int]) -> None:
    expected = sorted(sequence)
    sorter = SORTERS[method_id]
    result, comparisons, _swaps = sorter(sequence)
    assert result == expected
    assert comparisons >= 0


def test_golden_fixed_result() -> None:
    inp, expected = GOLDEN
    for method_id, sorter in SORTERS.items():
        result, _, _ = sorter(inp)
        assert result == expected, method_id


def test_input_not_mutated() -> None:
    original = [3, 1, 2]
    snapshot = original.copy()
    for sorter in SORTERS.values():
        sorter(original)
        assert original == snapshot
