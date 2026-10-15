def sort_merge(data: list[int]) -> tuple[list[int], int, int | None]:
    arr = data.copy()
    state = {"comparisons": 0}

    def merge_sort(slice_arr: list[int]) -> list[int]:
        if len(slice_arr) <= 1:
            return slice_arr
        mid = len(slice_arr) // 2
        left = merge_sort(slice_arr[:mid])
        right = merge_sort(slice_arr[mid:])
        return merge(left, right)

    def merge(left: list[int], right: list[int]) -> list[int]:
        result: list[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            state["comparisons"] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_arr = merge_sort(arr)
    return sorted_arr, state["comparisons"], None
