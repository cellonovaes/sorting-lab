def sort_heap(data: list[int]) -> tuple[list[int], int, int | None]:
    arr = data.copy()
    comparisons = 0
    swaps = 0
    n = len(arr)

    def swap(i: int, j: int) -> None:
        nonlocal swaps
        arr[i], arr[j] = arr[j], arr[i]
        swaps += 1

    def heapify(size: int, root: int) -> None:
        nonlocal comparisons
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < size:
            comparisons += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < size:
            comparisons += 1
            if arr[right] > arr[largest]:
                largest = right
        if largest != root:
            swap(root, largest)
            heapify(size, largest)

    if n > 1:
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        for end in range(n - 1, 0, -1):
            swap(0, end)
            heapify(end, 0)
    return arr, comparisons, swaps
