class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add_in_tail(self, item: Node):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val, all=False):
        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            if curr_node.value == val:
                next_node = curr_node.next
                if next_node is None:
                    self.tail = prev_node
                    prev_node.next = None
                    return None
                if curr_node == self.head:
                    self.head = next_node
                    curr_node = next_node
                else:
                    prev_node.next = next_node
                    curr_node = next_node
                if not all:
                    return None
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def clean(self):
        self.head = None
        self.tail = None

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def len(self):
        ctr = 0
        node = self.head
        while node is not None:
            ctr += 1
            node = node.next
        return ctr

    def insert(self, afterNode: Node, newNode: Node):
        currNode = self.head
        while currNode is not None:
            if currNode == afterNode:
                nextNode = currNode.next
                newNode.next = nextNode
                currNode.next = newNode

                if self.head == self.tail:
                    self.tail = newNode
                if self.tail == afterNode:
                    self.tail = newNode

                return None
            currNode = currNode.next

    def as_list(self):
        list_ = []
        node = self.head
        while node is not None:
            list_.append(node.value)
            node = node.next

        return list_


def create_linked_list(list_of_values):
    linked_list = LinkedList()

    list_length = len(list_of_values)
    if list_length == 0:
        return linked_list

    left_value = list_of_values[0]
    left_node = Node(left_value)

    linked_list.head = left_node

    right_node = None

    for value_index in range(1, list_length):
        curr_value = list_of_values[value_index]

        right_node = Node(curr_value)
        left_node.next = right_node

        left_node = right_node

    linked_list.tail = right_node if right_node is not None else left_node

    return linked_list


def sum_linked_lists(first_ll: LinkedList, second_ll: LinkedList):
    if not first_ll.len() == second_ll.len():
        return None

    summed_values = []
    first_node = first_ll.head
    second_node = second_ll.head
    while first_node is not None:
        sum_values = first_node.value + second_node.value
        summed_values.append(sum_values)
        first_node = first_node.next
        second_node = second_node.next

    summed_linked_list = create_linked_list(summed_values)

    return summed_linked_list
