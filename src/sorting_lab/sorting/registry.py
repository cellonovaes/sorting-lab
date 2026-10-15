from sorting_lab.sorting.algorithms import (
    sort_bubble,
    sort_heap,
    sort_insertion,
    sort_merge,
    sort_quick,
    sort_selection,
    sort_tim,
)
from sorting_lab.sorting.types import SortFn

METHOD_NAMES: dict[str, str] = {
    "bubble": "Bubble Sort",
    "selection": "Selection Sort",
    "insertion": "Insertion Sort",
    "merge": "Merge Sort",
    "quick": "Quick Sort",
    "heap": "Heap Sort",
    "tim": "Tim Sort",
}

SORTERS: dict[str, SortFn] = {
    "bubble": sort_bubble,
    "selection": sort_selection,
    "insertion": sort_insertion,
    "merge": sort_merge,
    "quick": sort_quick,
    "heap": sort_heap,
    "tim": sort_tim,
}

METHOD_IDS: tuple[str, ...] = tuple(SORTERS.keys())
