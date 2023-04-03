class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        template = "[Node ({node_id}): value={value}, next={next}]"
        string_representation = template.format(
            node_id=id(self),
            value=f"{self.value}",
            next=f"{self.next.value}|{id(self.next)}" if self.next is not None else "None"
        )
        return string_representation

    def __repr__(self):
        return self.__str__()


class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.counter = 0

    def __len__(self):
        return self.counter

    def size(self):
        return len(self)

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
        else:
            tail = self.tail
            tail.next = new_node
        self.tail = new_node
        self.counter += 1

    def dequeue(self):
        if self.size() == 0:
            return None
        head = self.head
        if head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = head.next
        self.counter -= 1
        return head.value
