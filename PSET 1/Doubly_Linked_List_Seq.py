class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return "-".join([("(%s)" % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_head = Doubly_Linked_List_Node(x)
        new_head.next = self.head
        if self.head:
            self.head.prev = new_head
        if not self.tail:
            self.tail = new_head
        self.head = new_head

    def insert_last(self, x):
        new_tail = Doubly_Linked_List_Node(x)
        new_tail.prev = self.tail
        if self.tail:
            self.tail.next = new_tail
        if not self.head:
            self.head = new_tail
        self.tail = new_tail

    def delete_first(self):
        assert self.head
        x = self.head.item
        self.head = self.head.next
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        return x

    def delete_last(self):
        assert self.tail
        x = self.tail.item
        self.tail = self.tail.prev
        if not self.tail:
            self.head = None
        else:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head, L2.tail = x1, x2
        left, right = x1.prev, x2.next
        if left:
            left.next = right
        else:
            self.head = right
        if right:
            right.prev = left
        else:
            self.tail = left
        L2.head.prev = L2.tail.next = None
        return L2

    def splice(self, x, L2):
        L2.head.prev = x
        if x.next:
            L2.tail.next = x.next
            x.next.prev = L2.tail
        else:
            self.tail = L2.tail
        x.next = L2.head
        L2.head = L2.tail = None
