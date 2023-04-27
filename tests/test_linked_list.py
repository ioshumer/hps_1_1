import pytest

from source.linked_list import Node, LinkedList


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


def test_linked_list_creation():
    values = []
    linked_list = create_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head is None
    assert linked_list.tail is None

    values = [1]
    linked_list = create_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[0]

    values = [1, 2]
    linked_list = create_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[-1]

    values = [1, 3, 5, 13, 33, 55]
    linked_list = create_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[-1]


def test_add_in_tail():
    linked_list = create_linked_list([1, 2, 3])
    new_node = Node(15)
    linked_list.add_in_tail(new_node)
    assert linked_list.tail == new_node

    linked_list = LinkedList()
    new_node = Node(15)
    linked_list.add_in_tail(new_node)
    assert linked_list.head == new_node
    assert linked_list.tail == new_node


def test_find():
    linked_list = create_linked_list([1, 2, 3])

    first_value = 15
    first_node = Node(first_value)
    linked_list.add_in_tail(first_node)
    second_value = 33
    second_node = Node(33)
    linked_list.add_in_tail(second_node)

    first_finded = linked_list.find(first_value)
    assert first_finded == first_node

    second_finded = linked_list.find(second_value)
    assert second_finded == second_node

    unknown_node = Node(333)
    unknown_finded = linked_list.find(unknown_node)
    assert unknown_finded is None


@pytest.mark.parametrize(
    ('values_list'),
    [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4, 5]
    ]
)
def test_length(values_list):
    linked_list = create_linked_list(values_list)
    assert linked_list.len() == len(values_list)


def test_insert():
    linked_list = LinkedList()
    n1 = Node(1)
    linked_list.insert(None, n1)
    assert linked_list.head == n1
    assert linked_list.len() == 1

    linked_list = LinkedList()
    n1 = Node(1)
    linked_list.add_in_tail(n1)
    assert linked_list.head == n1
    assert linked_list.tail == n1
    n2 = Node(2)
    linked_list.insert(n1, n2)
    assert linked_list.head == n1
    assert linked_list.tail == n2
    assert linked_list.head.next == n2
    assert linked_list.tail == n2
    assert linked_list.tail.next is None

    values = [1, 2, 3]
    linked_list = create_linked_list(values)
    value_1 = 5
    n1 = Node(value_1)
    value_2 = 15
    n2 = Node(value_2)
    tail = linked_list.tail
    linked_list.insert(tail, n2)
    linked_list.insert(tail, n1)
    assert n1.next == n2


def test_sum_lists():
    first_list_of_values = []
    second_list_of_values = []
    first_linked_list = create_linked_list(first_list_of_values)
    second_linked_list = create_linked_list(second_list_of_values)
    summed_ll = sum_linked_lists(first_linked_list, second_linked_list)
    assert summed_ll.as_list() == []

    first_list_of_values = [1]
    second_list_of_values = [10]
    first_linked_list = create_linked_list(first_list_of_values)
    second_linked_list = create_linked_list(second_list_of_values)
    summed_ll = sum_linked_lists(first_linked_list, second_linked_list)
    assert summed_ll.as_list() == [11]

    first_list_of_values = [1, 2, 3, 4, 5]
    second_list_of_values = [10, 20, 30, 40, 50]
    first_linked_list = create_linked_list(first_list_of_values)
    second_linked_list = create_linked_list(second_list_of_values)
    summed_ll = sum_linked_lists(first_linked_list, second_linked_list)
    assert summed_ll.as_list() == [11, 22, 33, 44, 55]


def test_delete():
    linked_list = create_linked_list([])
    linked_list.delete(Node(10), all=True)

    linked_list = create_linked_list([1])
    linked_list.delete(1, all=True)
    assert linked_list.len() == 0

    linked_list = create_linked_list([1, 1])
    linked_list.delete(1, all=True)
    assert linked_list.len() == 0
    assert linked_list.tail is None
    assert linked_list.head is None

    linked_list = create_linked_list([1, 1])
    linked_list.delete(1, all=False)
    assert linked_list.len() == 1
    assert linked_list.tail.value == 1
    assert linked_list.head.value == 1

    linked_list = create_linked_list([1, 2])
    linked_list.delete(1)
    assert linked_list.len() == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2

    linked_list = create_linked_list([1, 1, 2])
    linked_list.delete(1, all=True)
    assert linked_list.len() == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2

    linked_list = create_linked_list([1, 1, 2])
    linked_list.delete(1, all=False)
    assert linked_list.len() == 2
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2

    linked_list = create_linked_list([1, 2, 2])
    linked_list.delete(2, all=True)
    assert linked_list.len() == 1
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1

    linked_list = create_linked_list([1, 2, 2])
    linked_list.delete(2, all=False)
    assert linked_list.len() == 2
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2

    linked_list = create_linked_list([1, 2, 3, 4, 5, 5])
    new_node = Node(5)
    linked_list.add_in_tail(new_node)
    assert linked_list.tail == new_node

    linked_list.delete(5, all=True)
    assert linked_list.tail.value == 4
    assert linked_list.as_list() == [1, 2, 3, 4]
