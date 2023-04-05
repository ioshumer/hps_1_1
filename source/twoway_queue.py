class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class TwoWayQueue:
    def __init__(self):
        self.front: Node = None
        self.tail: Node = None
        self.count = 0

    def addFront(self, item):
        node = Node(item)
        if self.front is None:
            self.tail = node
        else:
            front = self.front
            node.next = front
            front.prev = node
        self.front = node
        self.count += 1

    def addTail(self, item):
        node = Node(item)
        if self.tail is None:
            self.front = node
        else:
            tail = self.tail
            node.prev = tail
            tail.next = node
        self.tail = node
        self.count += 1

    def removeFront(self):
        if self.count == 0:
            return None
        node = self.front
        if self.front.next is None:
            self.front = self.tail = None
        else:
            next_to_front = self.front.next
            next_to_front.prev = None
            self.front = next_to_front
        self.count -= 1
        return node.value

    def removeTail(self):
        if self.count == 0:
            return None
        node = self.tail
        if self.tail.prev is None:
            self.front = self.tail = None
        else:
            prev_to_tail = self.tail.prev
            prev_to_tail.next = None
            self.tail = prev_to_tail
        self.count -= 1
        return node.value

    def size(self):
        return self.count
