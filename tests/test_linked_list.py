import pytest

from source.linked_list import Node, LinkedList, create_linked_list, sum_linked_lists


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
    linked_list.head = n1
    linked_list.tail = n1

    n2 = Node(3)
    linked_list.insert(n1, n2)

    assert linked_list.head.next == n2
    assert linked_list.tail == n2

    values = [1, 2, 3]
    linked_list = create_linked_list(values)
    value_1 = 5
    n_1 = Node(value_1)
    value_2 = 15
    n2 = Node(value_2)

    tail = linked_list.tail
    linked_list.insert(tail, n2)
    linked_list.insert(tail, n1)

    assert n1.next == n2


def test_sum_lists():
    first_list_of_values = [1, 2, 3, 4, 5]
    second_list_of_values = [10, 20, 30, 40, 50]

    first_linked_list = create_linked_list(first_list_of_values)
    second_linked_list = create_linked_list(second_list_of_values)

    summed_ll = sum_linked_lists(first_linked_list, second_linked_list)

    assert summed_ll.as_list() == [11, 22, 33, 44, 55]
