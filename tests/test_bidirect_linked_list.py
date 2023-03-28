from typing import List

import pytest

from source.bidirect_linked_list import create_from_values, Node, create_from_nodes


def test_list_creation():
    values = []
    linked_list = create_from_values(values)
    assert values == linked_list.as_list()
    assert linked_list.head is None
    assert linked_list.tail is None

    values = [1]
    linked_list = create_from_values(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[0]

    values = [1, 2]
    linked_list = create_from_values(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[-1]

    values = [1, 3, 5, 13, 33, 55]
    linked_list = create_from_values(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[-1]


@pytest.mark.parametrize(
    ('list_of_nodes', 'as_list', 'head_value', 'tail_value'),
    [
        ([], [], None, None),
        ([Node(1)], [1], 1, 1),
        ([Node(1), Node(2)], [1, 2], 1, 2),
        ([Node(1), Node(2), Node(3)], [1, 2, 3], 1, 3),
    ]
)
def test_creation_by_nodes(list_of_nodes, as_list, head_value, tail_value):
    linked_list = create_from_nodes(list_of_nodes)
    assert linked_list.as_list() == as_list

    try:
        assert linked_list.head.value == head_value
    except AttributeError:
        assert linked_list.head == head_value

    try:
        assert linked_list.tail.value == tail_value
    except AttributeError:
        assert linked_list.head == tail_value


@pytest.mark.parametrize(
    ('values', 'finding_value', 'result'),
    [
        ([], 1, None),
        ([1], 1, 1),
        ([1, 2], 1, 1),
        ([1, 2], 2, 2),
        ([2, 2], 2, 2),
        ([2, 1, 2], 1, 1),
    ]
)
def test_find(values, finding_value, result):
    linked_list = create_from_values(values)
    found_node = linked_list.find(finding_value)
    if found_node is None:
        assert result is None
    else:
        assert found_node.value == result


@pytest.mark.parametrize(
    ('list_of_nodes', 'node_index', 'node_value'),
    [
        ([], 1, None),
        ([Node(1)], 0, 1),
        ([Node(1), Node(2)], 0, 1),
        ([Node(1), Node(2)], 1, 2),
        ([Node(1), Node(2), Node(3)], 1, 2),
        ([Node(1), Node(2), Node(3)], 2, 3)
    ]
)
def test_getting_by_node_index(list_of_nodes, node_index, node_value):
    linked_list = create_from_nodes(list_of_nodes)
    node = linked_list.get_node_by_index(node_index)
    try:
        assert node.value == node_value
    except AttributeError:
        assert node == node_value


@pytest.mark.parametrize(
    ('values', 'finding_value', 'result'),
    [
        ([], 1, []),
        ([1], 1, [1]),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([2, 2], 2, [2, 2]),
        ([2, 1, 2], 1, [1]),
        ([2, 1, 2], 2, [2, 2]),
    ]
)
def test_find_all(values, finding_value, result):
    linked_list = create_from_values(values)
    found_result = [node.value for node in linked_list.find_all(finding_value)]
    assert found_result == result


@pytest.mark.parametrize(
    ('linked_list_values', 'value_to_delete', 'all_', 'as_list', 'head_value', 'tail_value', 'length'),
    [
        ([], 13, False, [], None, None, 0),
        ([], 13, True, [], None, None, 0),
        ([13], 1, False, [13], 13, 13, 1),
        ([13], 1, True, [13], 13, 13, 1),
        ([13], 13, False, [], None, None, 0),
        ([13], 13, True, [], None, None, 0),
        ([13, 13], 1, False, [13, 13], 13, 13, 2),
        ([13, 13], 1, True, [13, 13], 13, 13, 2),
        ([13, 13], 13, False, [13], 13, 13, 1),
        ([13, 13], 13, True, [], None, None, 0),
        ([13, 13, 100], 13, False, [13, 100], 13, 100, 2),
        ([13, 13, 100], 13, True, [100], 100, 100, 1),
        ([13, 13, 100], 100, False, [13, 13], 13, 13, 2),
        ([13, 13, 100, 100], 13, False, [13, 100, 100], 13, 100, 3),
        ([13, 13, 100, 100], 100, False, [13, 13, 100], 13, 100, 3),
        ([13, 13, 100, 100], 100, True, [13, 13], 13, 13, 2),
        ([13, 13, 100, 100, 404, 404], 100, False, [13, 13, 100, 404, 404], 13, 404, 5),
        ([13, 13, 100, 100, 404, 404], 100, True, [13, 13, 404, 404], 13, 404, 4)
    ]
)
def test_delete(linked_list_values, value_to_delete, all_, as_list, tail_value, head_value, length):
    linked_list = create_from_values(linked_list_values)
    linked_list.delete(value_to_delete, all=all_)
    assert linked_list.as_list() == as_list
    if linked_list.head is not None:
        assert linked_list.head.value == head_value
    else:
        assert linked_list.head is head_value
    if linked_list.tail is not None:
        assert linked_list.tail.value == tail_value
    else:
        assert linked_list.tail is tail_value
    assert linked_list.len() == length


@pytest.mark.parametrize(
    ('list_of_nodes', 'new_node', 'head_value', 'tail_value', 'as_list'),
    [
        ([], Node(1), 1, 1, [1]),
        ([Node(2)], Node(1), 1, 2, [1, 2]),
        ([Node(2), Node(3)], Node(1), 1, 3, [1, 2, 3]),
    ]
)
def test_add_in_head(list_of_nodes, new_node, head_value, tail_value, as_list):
    linked_list = create_from_nodes(list_of_nodes)
    linked_list.add_in_head(new_node)
    assert linked_list.head.value == head_value
    assert linked_list.tail.value == tail_value
    assert linked_list.as_list() == as_list


@pytest.mark.parametrize(
    ('linked_list_values', 'list_type', 'after_node', 'new_node', 'head_value', 'tail_value', 'as_list', 'length'),
    [
        ([], 'int', None, Node(13), 13, 13, [13], 1),
        ([Node(1)], 'nodes', None, Node(13), 1, 13, [1, 13], 2),
    ]
)
def test_insert_empty(linked_list_values, list_type, after_node, new_node, head_value, tail_value, as_list, length):
    if list_type == 'int':
        linked_list = create_from_values(linked_list_values)
    elif list_type == 'nodes':
        linked_list = create_from_nodes(linked_list_values)
    linked_list.insert(after_node, new_node)
    assert linked_list.head.value == head_value
    assert linked_list.tail.value == tail_value
    assert linked_list.as_list() == as_list
    assert linked_list.len() == length


@pytest.mark.parametrize(
    ('linked_list_values', 'after_node_idx', 'new_node', 'head_value', 'tail_value', 'as_list', 'length'),
    [
        ([], None, Node(5), 5, 5, [5], 1),
        ([Node(3)], 0, Node(5), 3, 5, [3, 5], 2),
        ([Node(3), Node(5)], 0, Node(4), 3, 5, [3, 4, 5], 3),
    ]
)
def test_insert_positioned(
        linked_list_values: List[Node], after_node_idx, new_node: Node, head_value, tail_value, as_list, length
):
    linked_list = create_from_nodes(linked_list_values)
    after_node = linked_list.get_node_by_index(after_node_idx) if after_node_idx is not None else None
    next_of_after_node = after_node.next if after_node_idx is not None else None
    linked_list.insert(after_node, new_node)
    assert linked_list.head.value == head_value if linked_list.head is not None else linked_list.head == head_value
    assert linked_list.tail.value == tail_value if linked_list.tail is not None else linked_list.tail == tail_value
    if after_node:
        assert after_node.next == new_node
    if next_of_after_node:
        assert next_of_after_node.prev == new_node
    assert new_node.prev == after_node
    assert new_node.next == next_of_after_node


@pytest.mark.parametrize(
    ('linked_list_values', 'as_list', 'length'),
    [
        ([], [], 0),
        ([1], [], 0),
        ([1, 2], [], 0),
        ([1, 2, 3], [], 0),
    ]
)
def test_clean(linked_list_values, as_list, length):
    linked_list = create_from_values(linked_list_values)
    linked_list.clean()
    assert linked_list.as_list() == as_list
    assert linked_list.len() == 0