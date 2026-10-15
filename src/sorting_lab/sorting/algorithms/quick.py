def sort_quick(data: list[int]) -> tuple[list[int], int, int | None]:
    arr = data.copy()
    comparisons = 0
    swaps = 0

    def swap(i: int, j: int) -> None:
        nonlocal swaps
        arr[i], arr[j] = arr[j], arr[i]
        swaps += 1

    def median_of_three(low: int, high: int) -> int:
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        if a > b:
            if b > c:
                return mid
            return high if a > c else low
        if a > c:
            return low
        return high if b > c else mid

    def partition(low: int, high: int) -> int:
        nonlocal comparisons
        pivot_idx = median_of_three(low, high)
        swap(pivot_idx, high)
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    swap(i, j)
        swap(i + 1, high)
        return i + 1

    def quick_sort(low: int, high: int) -> None:
        if low < high:
            p = partition(low, high)
            quick_sort(low, p - 1)
            quick_sort(p + 1, high)

    if arr:
        quick_sort(0, len(arr) - 1)
    return arr, comparisons, swaps
