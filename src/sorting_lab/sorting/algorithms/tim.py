RUN = 32


def sort_tim(data: list[int]) -> tuple[list[int], int, int | None]:
    arr = data.copy()
    comparisons = 0
    n = len(arr)

    def insertion_sort_range(left: int, right: int) -> None:
        nonlocal comparisons
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left:
                comparisons += 1
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break
            arr[j + 1] = key

    def merge(left: int, mid: int, right: int) -> None:
        nonlocal comparisons
        left_part = arr[left : mid + 1]
        right_part = arr[mid + 1 : right + 1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            comparisons += 1
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1

    if n == 0:
        return arr, 0, None

    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        insertion_sort_range(start, end)

    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(left, mid, right)
        size *= 2

    return arr, comparisons, None
