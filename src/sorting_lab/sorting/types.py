from dataclasses import dataclass
from typing import Callable

SortFn = Callable[[list[int]], tuple[list[int], int, int | None]]

MAX_SEQUENCE_LENGTH = 10_000


@dataclass(frozen=True)
class SortRunResult:
    method: str
    sorted: list[int]
    time_ms: float
    comparisons: int
    swaps: int | None
