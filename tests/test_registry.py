import pytest

from sorting_lab.sorting.engine import SequenceValidationError, sort_sequence


def test_all_returns_seven_results() -> None:
    results = sort_sequence([5, 3, 1], "all")
    assert len(results) == 7
    expected = [1, 3, 5]
    assert all(run.sorted == expected for run in results)


def test_single_method() -> None:
    results = sort_sequence([2, 1], "merge")
    assert len(results) == 1
    assert results[0].method == "merge"
    assert results[0].sorted == [1, 2]


def test_validation_non_integer() -> None:
    with pytest.raises(SequenceValidationError):
        sort_sequence([1, 2.5], "bubble")


def test_validation_oversize() -> None:
    with pytest.raises(SequenceValidationError):
        sort_sequence(list(range(10_001)), "bubble")


def test_unknown_method() -> None:
    with pytest.raises(SequenceValidationError):
        sort_sequence([1], "radix")
