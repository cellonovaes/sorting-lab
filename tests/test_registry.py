import pytest

from sorting_lab.sorting.engine import SequenceValidationError, sort_sequence
from sorting_lab.sorting.registry import (
    METHOD_IDS,
    METHOD_META,
    QUADRATIC_METHOD_IDS,
    list_method_meta,
    needs_large_n_warning,
)


def test_educational_metadata_complete() -> None:
    metas = list_method_meta()
    assert len(metas) == 7
    assert tuple(m.id for m in metas) == METHOD_IDS
    for meta in metas:
        assert meta.name
        assert meta.complexity_best
        assert meta.complexity_average
        assert meta.complexity_worst
        assert isinstance(meta.stable, bool)
        assert meta.blurb.strip()
        assert meta.id in METHOD_META


def test_quadratic_family_average() -> None:
    for mid in QUADRATIC_METHOD_IDS:
        avg = METHOD_META[mid].complexity_average
        assert "n²" in avg or "n^2" in avg


def test_large_n_warning_helper() -> None:
    assert needs_large_n_warning("all", 1000) is True
    assert needs_large_n_warning("bubble", 1000) is True
    assert needs_large_n_warning("merge", 1000) is False
    assert needs_large_n_warning("all", 999) is False


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
