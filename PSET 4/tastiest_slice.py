from Set_AVL_Tree import BST_Node, Set_AVL_Tree

#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################


class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return "%s,%s" % (self.key, self.val)


class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()

        # `sum` subtree augmentation
        A.sum = (
            A.item.val + (A.left.sum if A.left else 0) + (A.right.sum if A.right else 0)
        )

        # `max_prefix` subtree augmentation
        if not A.left and not A.right:
            A.max_prefix = A.item.val
            A.max_prefix_key = A.item.key
        elif A.left and not A.right:
            left, middle = (A.left.max_prefix, A.left.sum + A.item.val)
            A.max_prefix = max(left, middle)
            if left == A.max_prefix:
                A.max_prefix_key = A.left.max_prefix_key
            else:
                A.max_prefix_key = A.item.key
        elif not A.left and A.right:
            middle, right = (A.item.val, A.item.val + A.right.max_prefix)
            A.max_prefix = max(middle, right)
            if right == A.max_prefix:
                A.max_prefix_key = A.right.max_prefix_key
            else:
                A.max_prefix_key = A.item.key
        else:
            left, middle, right = (
                A.left.max_prefix,
                A.left.sum + A.item.val,
                A.left.sum + A.item.val + A.right.max_prefix,
            )
            A.max_prefix = max(left, middle, right)
            if left == A.max_prefix:
                A.max_prefix_key = A.left.max_prefix_key
            elif middle == A.max_prefix:
                A.max_prefix_key = A.item.key
            else:
                A.max_prefix_key = A.right.max_prefix_key


class Part_B_Tree(Set_AVL_Tree):
    def __init__(self):
        super().__init__(Part_B_Node)

    def max_prefix(self):
        """
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        """
        # Access subtree augmentations in O(1) time
        k = self.root.max_prefix_key
        s = self.root.max_prefix
        return (k, s)


def tastiest_slice(toppings):
    """
    Input:  toppings | List of integer tuples (x,y,t) representing
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice
                     | at (X,Y) with tastiness T
    """
    B = Part_B_Tree()  # use data structure from part (b)
    X, Y, T = 0, 0, 0
    # Sort in O(n log n) time
    toppings.sort(key=lambda t: t[0])
    for x, y, t in toppings:
        # O(log n) time Set AVL insertion
        B.insert(Key_Val_Item(y, t))
        # O(1) time subtree augmentation access
        k, s = B.max_prefix()
        if s > T:
            X, Y, T = x, k, s
    return (X, Y, T)
