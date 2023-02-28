#!/usr/bin/env python3


def get_damages(H: list[int]) -> list[int]:
    """
    Modified merge sort algorithm that returns the damage hash list, D

    >>> H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]
    >>> get_damages(H)
    [4, 5, 6, 3, 3, 1, 4, 1, 1, 1]
    """
    D = [1 for _ in H]  # O(n)
    H_idx = [(h, idx) for idx, h in enumerate(H)]  # O(n)

    def inversion_merge_sort(H_idx: list[tuple[int]]) -> list[tuple[int]]:
        if len(H_idx) < 2:
            return H_idx

        pivot = len(H_idx) // 2
        left, right = (
            inversion_merge_sort(H_idx[:pivot]),
            inversion_merge_sort(H_idx[pivot:]),
        )

        # The merge/non-recursive step is O(n)
        result, j, incr = [], 0, 0
        for i, h in enumerate(left):
            while j < len(right) and right[j][0] < left[i][0]:
                result.append(right[j])
                incr += 1
                j += 1
            result.append(left[i])
            D[left[i][1]] += incr

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    # T(n) = 2T(n/2) + O(n) = O(n log n)
    inversion_merge_sort(H_idx)
    return D
