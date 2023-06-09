class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head: Node = None
        self.tail: Node = None
        self.counter = 0
        self.__ascending = asc

    def _compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    @property
    def asc(self):
        return self.__ascending

    def compare(self, v1, v2):
        return self._compare(v1, v2)

    def insert_to_the_left(self, new_node: Node, pointer: Node):
        if pointer.prev is not None:
            pointer_prev = pointer.prev
            pointer_prev.next = new_node
            new_node.prev = pointer_prev
        pointer.prev = new_node
        new_node.next = pointer
        if pointer is self.head:
            self.head = new_node

    def insert_to_the_right(self, new_node: Node, pointer: Node):
        pointer.next = new_node
        new_node.prev = pointer

        if pointer is self.tail:
            self.tail = new_node

    def add(self, value):
        new_node = Node(value)

        pointer = self.head

        if pointer is None:
            self.head = self.tail = new_node
            self.counter += 1
            return

        while pointer is not None:
            if (self.asc and self.compare(new_node.value, pointer.value) <= 0) or \
                    (not self.asc and self.compare(new_node.value, pointer.value) >= 0):
                self.insert_to_the_left(new_node, pointer)
                self.counter += 1
                return
            else:
                if pointer.next is None:
                    self.insert_to_the_right(new_node, pointer)
                    self.counter += 1
                    return
                pointer = pointer.next

        self.insert_to_the_right(new_node, pointer)
        self.counter += 1
        return

    def find(self, val):
        pointer = self.head
        if (self.asc and self.compare(val, pointer.value) == -1) or \
                (not self.asc and self.compare(val, pointer.value) == 1):
            return None
        while pointer is not None:
            if pointer.value == val:
                return pointer
            pointer = pointer.next

    def delete(self, val):
        pointer = self.head

        if pointer is None:
            return None

        while pointer is not None:
            if pointer.value == val:
                if pointer is self.head and pointer is self.tail:
                    self.head = self.tail = None
                elif pointer.value == val and pointer is self.head:
                    next_to_head = self.head.next
                    next_to_head.prev = None
                    self.head = next_to_head
                elif pointer.value == val and pointer is self.tail:
                    prev_to_tail = self.tail.prev
                    prev_to_tail.next = None
                    self.tail = prev_to_tail
                elif pointer.value == val:
                    prev = pointer.prev
                    next = pointer.next
                    prev.next = next
                    next.prev = prev
                else:
                    raise BaseException("Untracked case")
                self.counter -= 1
                return
            else:
                pointer = pointer.next

    def clean(self, asc):
        self.__ascending = asc
        self.tail = self.head = None
        self.counter = 0

    def len(self):
        return self.counter

    def get_all(self, asc=True):
        r = []
        if asc:
            node = self.head
            while node is not None:
                r.append(node)
                node = node.next
        else:
            node = self.tail
            while node is not None:
                r.append(node)
                node = node.prev
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip(' ')
        v2 = v2.strip(' ')
        return self._compare(v1, v2)
