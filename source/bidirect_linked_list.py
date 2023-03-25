class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node

            node = node.next

    def find_all(self, val):
        return []  # здесь будет ваш код

    def delete(self, val, all=False):
        pass  # здесь будет ваш код

    def clean(self):
        pass  # здесь будет ваш код

    def len(self):
        return 0  # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass  # здесь будет ваш код

    def add_in_head(self, newNode):
        pass  # здесь будет ваш код


def create_bidirect_linked_list(list_of_values):
    values_amount = len(list_of_values)

    if len(values_amount) == 0:
        return LinkedList2


