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
        return None

    def find_all(self, val):
        finded_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                finded_nodes.append(node)
            node = node.next
        return finded_nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node is self.head:
                    if node.next is None:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = node.next
                elif node is self.tail:
                    prev = self.tail.prev
                    prev.next = None
                    self.tail = prev
                else:
                    prev = node.prev
                    next = node.next
                    if prev:
                        prev.next = next
                    if next:
                        next.prev = prev

                if not all:
                    break

            node = node.next

    def clean(self):
        pass  # здесь будет ваш код

    def len(self):
        ctr = 0
        node = self.head
        while node is not None:
            ctr += 1
            node = node.next
        return ctr

    def insert(self, afterNode, newNode):
        pass  # здесь будет ваш код

    def add_in_head(self, newNode):
        pass  # здесь будет ваш код

    def as_list(self):
        node_values = []
        node = self.head
        while node is not None:
            node_values.append(node.value)
            node = node.next
        return node_values


def create_bidirect_linked_list(list_of_values):
    linked_list = LinkedList2()

    values_amount = len(list_of_values)
    if values_amount == 0:
        return linked_list

    left_value = list_of_values[0]
    left_node = Node(left_value)

    linked_list.add_in_tail(left_node)

    for value_index in range(1, values_amount):
        value = list_of_values[value_index]
        new_node = Node(value)
        linked_list.add_in_tail(new_node)

    return linked_list
