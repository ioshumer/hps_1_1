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

    def find(self, val) -> Node:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val, all=False):
        node = self.head
        prev_node = None

        while node is not None:
            if node.value == val:
                if self.head == self.tail == node:
                    self.head = self.tail = None
                elif self.head == node:
                    self.head = node.next
                elif self.tail == node:
                    prev_node.next = None
                    self.tail = prev_node
                elif prev_node is not None:
                    prev_node.next = node.next

                if not all:
                    break
            else:
                prev_node = node

            node = node.next

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
        if afterNode is None:
            self.add_in_tail(newNode)
            return None

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
