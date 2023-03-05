#!/usr/bin/env python3


def merge_adjacent_bookings(
    B: tuple[tuple[int, int, int]]
) -> tuple[tuple[int, int, int]]:
    """
    Returns booking schedule with adjacent bookings having same number of rooms merged

    >>> B = ((2, 0, 2), (2, 2, 4), (2, 4, 10))
    >>> merge_adjacent_bookings(B)
    ((2, 0, 10),)
    """
    j, new_B = 1, [B[0]]
    while j < len(B):
        left_k, left_start, left_end = new_B[-1]
        right_k, right_start, right_end = (new_b := B[j])
        if j < len(B) and left_k == right_k and left_end == right_start:
            new_B.pop()
            new_b = (left_k, left_start, right_end)
        new_B.append(new_b)
        j += 1
    return tuple(new_B)


def merge_booking_schedules(
    B1: tuple[tuple[int, int, int]], B2: tuple[tuple[int, int, int]]
) -> tuple[tuple[int, int, int]]:
    """
    Returns merged booking schedule from booking schedules B1, B2

    >>> B1 = ((2, 1, 6), (1, 6, 7), (3, 10, 12))
    >>> B2 = ((1, 0, 4), (5, 4, 6))
    >>> merge_booking_schedules(B1, B2)
    ((1, 0, 1), (3, 1, 4), (7, 4, 6), (1, 6, 7), (3, 10, 12))
    >>> B1 = ((1, 2, 3),)
    >>> B2 = ((1, 4, 10),)
    >>> merge_booking_schedules(B1, B2)
    ((1, 2, 3), (1, 4, 10))
    """
    B, i, j = [], 0, 0
    B1_not_exhausted = (b1_idx := i // 2) < len(B1)
    B2_not_exhausted = (b2_idx := j // 2) < len(B2)
    b1_boundary = B1[b1_idx][i % 2 + 1] if B1_not_exhausted else float("inf")
    b2_boundary = B2[b2_idx][j % 2 + 1] if B2_not_exhausted else float("inf")
    while B1_not_exhausted or B2_not_exhausted:
        start = min(b1_boundary, b2_boundary)
        if b1_boundary <= b2_boundary:
            i += 1
            B1_not_exhausted = (b1_idx := i // 2) < len(B1)
            b1_boundary = B1[b1_idx][i % 2 + 1] if B1_not_exhausted else float("inf")
        else:
            j += 1
            B2_not_exhausted = (b2_idx := j // 2) < len(B2)
            b2_boundary = B2[b2_idx][j % 2 + 1] if B2_not_exhausted else float("inf")
        end = min(b1_boundary, b2_boundary)
        if start < end:
            b1_k, b1_start = B1[b1_idx][:2] if B1_not_exhausted else (0, float("inf"))
            b2_k, b2_start = B2[b2_idx][:2] if B2_not_exhausted else (0, float("inf"))
            k = (end > b1_start) * b1_k + (end > b2_start) * b2_k
            if k != 0:
                B.append((k, start, end))

    B = merge_adjacent_bookings(B)
    return tuple(B)


def satisfying_booking(R: tuple[tuple[int, int]]) -> tuple[tuple[int, int, int]]:
    """
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R

    >>> R = ((2, 3),)
    >>> satisfying_booking(R)
    ((1, 2, 3),)
    >>> R = ((2, 3), (4, 10), (2, 8), (6, 9), (0, 1), (1, 12), (13, 14))
    >>> satisfying_booking(R)
    ((1, 0, 2), (3, 2, 3), (2, 3, 4), (3, 4, 6), (4, 6, 8), (3, 8, 9), (2, 9, 10), (1, 10, 12), (1, 13, 14))
    >>> R = ((32, 89), (112, 390), (163, 247), (50, 75), (107, 385), (62, 276), (82, 312), (18, 104), (136, 351), (72, 170), (151, 356), (104, 175), (65, 161), (215, 345), (60, 179), (182, 269), (101, 212), (159, 278), (73, 144), (216, 242))
    >>> satisfying_booking(R)
    ((1, 18, 32), (2, 32, 50), (3, 50, 60), (4, 60, 62), (5, 62, 65), (6, 65, 72), (7, 72, 73), (8, 73, 75), (7, 75, 82), (8, 82, 89), (7, 89, 101), (8, 101, 107), (9, 107, 112), (10, 112, 136), (11, 136, 144), (10, 144, 151), (11, 151, 159), (12, 159, 161), (11, 161, 163), (12, 163, 170), (11, 170, 175), (10, 175, 179), (9, 179, 182), (10, 182, 212), (9, 212, 215), (10, 215, 216), (11, 216, 242), (10, 242, 247), (9, 247, 269), (8, 269, 276), (7, 276, 278), (6, 278, 312), (5, 312, 345), (4, 345, 351), (3, 351, 356), (2, 356, 385), (1, 385, 390))
    """
    if not R:
        return ((0, 0, 0),)
    if len(R) == 1:
        return ((1, *R[0]),)

    left, right = (
        satisfying_booking(R[: len(R) // 2]),
        satisfying_booking(R[len(R) // 2 :]),
    )
    return merge_booking_schedules(left, right)
