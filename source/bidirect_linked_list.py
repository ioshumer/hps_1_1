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
                        next_node = node.next
                        next_node.prev = None
                        self.head = next_node
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
        self.head = self.tail = None

    def len(self):
        ctr = 0
        node = self.head
        while node is not None:
            ctr += 1
            node = node.next
        return ctr

    def insert(self, afterNode, newNode):
        if afterNode is None and self.len() == 0:
            self.add_in_head(newNode)
        elif afterNode is None or afterNode == self.tail:
            self.add_in_tail(newNode)
        else:
            curr_node = self.head
            while curr_node is not None:
                if curr_node == afterNode:
                    next_of_curr = curr_node.next
                    newNode.prev = curr_node
                    newNode.next = next_of_curr
                    next_of_curr.prev = newNode
                    curr_node.next = newNode
                    break
                curr_node = curr_node.next

    def add_in_head(self, newNode: Node):
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
            self.tail = newNode
            return None

        curr_head = self.head
        curr_head.prev = newNode
        newNode.next = curr_head
        self.head = newNode

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


def create_from_values(list_of_values):
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


def create_from_nodes(list_of_nodes: List[Node]):
    linked_list = LinkedList2()

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
