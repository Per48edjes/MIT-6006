from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class L:
    value: int
    size: int
    next: Optional[L] = None


def reorder_students(L):
    """
    >>> students = L(0, 4, L(1, 3, L(2, 2, L(3, 1, None))))
    >>> node = students
    >>> while node:
    ...     print(node.value)
    ...     node = node.next
    0
    1
    2
    3
    >>> reorder_students(students)
    >>> node = students
    >>> while students:
    ...     print(students.value)
    ...     students = students.next
    0
    1
    3
    2
    """
    def reverse_ll(node: L) -> None:
        """
        Recursively reverse a linked list
        """
        if not node or not node.next:
            return node
        else:
            new_head = reverse_ll(node.next)
            node.next.next = node
            node.next = None
            return new_head

    # Traverse to the (n + 1)th student: O(n)
    nth_node = L
    for _ in range(L.size // 2 - 1):
        nth_node = nth_node.next
    n_plus_1_node = nth_node.next

    # Reverse second half of list: O(n)
    # ...and link to the first half: O(1)
    nth_node.next = reverse_ll(n_plus_1_node)
