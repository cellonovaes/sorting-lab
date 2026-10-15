from dataclasses import dataclass

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

QUADRATIC_METHOD_IDS: frozenset[str] = frozenset({"bubble", "selection", "insertion"})
LARGE_N_WARNING_THRESHOLD = 1_000


@dataclass(frozen=True)
class MethodMeta:
    id: str
    name: str
    complexity_best: str
    complexity_average: str
    complexity_worst: str
    stable: bool
    blurb: str


METHOD_META: dict[str, MethodMeta] = {
    "bubble": MethodMeta(
        id="bubble",
        name="Bubble Sort",
        complexity_best="O(n)",
        complexity_average="O(n²)",
        complexity_worst="O(n²)",
        stable=True,
        blurb=(
            "Percorre a lista trocando pares adjacentes fora de ordem até não "
            "haver mais trocas. Simples de entender, mas lento em entradas grandes."
        ),
    ),
    "selection": MethodMeta(
        id="selection",
        name="Selection Sort",
        complexity_best="O(n²)",
        complexity_average="O(n²)",
        complexity_worst="O(n²)",
        stable=False,
        blurb=(
            "Em cada passo escolhe o menor restante e o coloca na posição "
            "correta. Poucas trocas, porém sempre faz muitas comparações."
        ),
    ),
    "insertion": MethodMeta(
        id="insertion",
        name="Insertion Sort",
        complexity_best="O(n)",
        complexity_average="O(n²)",
        complexity_worst="O(n²)",
        stable=True,
        blurb=(
            "Insere cada elemento na posição correta da parte já ordenada. "
            "Rápido em listas quase ordenadas; degrada com entradas aleatórias grandes."
        ),
    ),
    "merge": MethodMeta(
        id="merge",
        name="Merge Sort",
        complexity_best="O(n log n)",
        complexity_average="O(n log n)",
        complexity_worst="O(n log n)",
        stable=True,
        blurb=(
            "Divide a lista ao meio, ordena as metades e as mescla. "
            "Garantia O(n log n), com custo extra de memória auxiliar."
        ),
    ),
    "quick": MethodMeta(
        id="quick",
        name="Quick Sort",
        complexity_best="O(n log n)",
        complexity_average="O(n log n)",
        complexity_worst="O(n²)",
        stable=False,
        blurb=(
            "Particiona em torno de um pivô (aqui, mediana de três) e ordena "
            "as partes. Em média muito rápido; o pior caso teórico ainda é O(n²)."
        ),
    ),
    "heap": MethodMeta(
        id="heap",
        name="Heap Sort",
        complexity_best="O(n log n)",
        complexity_average="O(n log n)",
        complexity_worst="O(n log n)",
        stable=False,
        blurb=(
            "Constrói um heap e extrai o máximo repetidamente. "
            "Limite O(n log n) in-place, mas não é estável."
        ),
    ),
    "tim": MethodMeta(
        id="tim",
        name="Tim Sort",
        complexity_best="O(n)",
        complexity_average="O(n log n)",
        complexity_worst="O(n log n)",
        stable=True,
        blurb=(
            "Híbrido estável (ideia do sorted() do Python): aproveita trechos "
            "já ordenados. Excelente no caso quase ordenado; aqui é uma versão didática."
        ),
    ),
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
METHOD_NAMES: dict[str, str] = {mid: METHOD_META[mid].name for mid in METHOD_IDS}


def list_method_meta() -> list[MethodMeta]:
    return [METHOD_META[mid] for mid in METHOD_IDS]


def needs_large_n_warning(method: str, n: int) -> bool:
    if n < LARGE_N_WARNING_THRESHOLD:
        return False
    if method == "all":
        return True
    return method in QUADRATIC_METHOD_IDS
