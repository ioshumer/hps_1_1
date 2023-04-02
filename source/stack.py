from typing import List


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __str__(self):
        template = "[Node ({node_id}): value={value}, prev={prev}, next={next}]"
        string_representation = template.format(
            node_id=id(self),
            value=f"{self.value}",
            prev=f"{self.prev.value}|{id(self.prev)}" if self.prev is not None else "None",
            next=f"{self.next.value}|{id(self.next)}" if self.next is not None else "None"
        )
        return string_representation

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.counter = 0

    def __len__(self):
        return self.counter

    def add_in_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.counter += 1

    def add_in_head(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.prev = None
            new_node.next = None
            self.tail = new_node
        else:
            head = self.head
            head.prev = new_node
            new_node.next = head
        self.head = new_node
        self.counter += 1

    def pop_from_tail(self):
        if self.tail is None:
            return None

        tail = self.tail

        if tail.prev is None:
            self.tail = None
        else:
            prev = tail.prev
            prev.next = None
            self.tail = prev

        self.counter -= 1
        return tail.value

    def pop_from_head(self):
        if self.head is None:
            return None

        head = self.head
        if head.next is None:
            self.head = None
        else:
            next = head.next
            next.prev = None
            self.head = next

        self.counter -= 1
        return head.value

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

    def as_list(self):
        node_values = []
        node = self.head
        while node is not None:
            node_values.append(node.value)
            node = node.next
        return node_values

    def get_node_by_index(self, index):
        ctr = 0
        node = self.head
        while node is not None:
            if ctr == index:
                return node
            ctr += 1
            node = node.next

    def get_head(self):
        return self.head.value

    def get_tail(self):
        return self.tail.value


def create_from_values(list_of_values):
    linked_list = DoublyLinkedList()

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


def create_from_nodes(list_of_nodes: List[Node]):
    linked_list = DoublyLinkedList()

    values_amount = len(list_of_nodes)
    if values_amount == 0:
        return linked_list

    if values_amount == 1:
        linked_list.head = list_of_nodes[0]
        linked_list.tail = list_of_nodes[0]
        return linked_list

    prev_node = list_of_nodes[0]
    linked_list.head = prev_node

    for node_idx in range(1, values_amount):
        curr_node = list_of_nodes[node_idx]
        prev_node.next = curr_node
        curr_node.prev = prev_node
        prev_node = curr_node

    linked_list.tail = curr_node

    return linked_list


class Stack:
    def __init__(self):
        self.stack = DoublyLinkedList()

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None
        item = self.stack.pop_from_head()
        return item

    def push(self, value):
        self.stack.add_in_head(value)

    def peek(self):
        return self.stack.get_head()

