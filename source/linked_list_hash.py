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


class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def hash_fun(self, value):
        byte_string = value.encode()
        hash_sum = sum(byte_string) % self.size
        return hash_sum

    def seek_slot(self, value):
        hash = self.hash_fun(value)
        hash_idx = hash
        return hash_idx

    def put(self, value):
        value = str(value)
        slot_idx = self.seek_slot(value)
        if self.slots[slot_idx] is None:
            linked_list = LinkedList()
            self.slots[slot_idx] = linked_list
        else:
            linked_list = self.slots[slot_idx]
        new_node = Node(value)
        linked_list.add_in_tail(new_node)
        return slot_idx

    def pop(self, value):
        ...

    def find(self, value):
        value = str(value)
        slot_idx = self.seek_slot(value)
        if slot_idx is None:
            return None

        linked_list = self.slots[slot_idx]
        is_in_slot = linked_list.find(value)

        return slot_idx if is_in_slot is not None else None
