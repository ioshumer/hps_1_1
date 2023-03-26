import pytest

from source.bidirect_linked_list import create_bidirect_linked_list


def test_list_creation():
    values = []
    linked_list = create_bidirect_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head is None
    assert linked_list.tail is None

    values = [1]
    linked_list = create_bidirect_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[0]

    values = [1, 2]
    linked_list = create_bidirect_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[-1]

    values = [1, 3, 5, 13, 33, 55]
    linked_list = create_bidirect_linked_list(values)
    assert values == linked_list.as_list()
    assert linked_list.head.value == values[0]
    assert linked_list.tail.value == values[-1]


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
    linked_list = create_bidirect_linked_list(values)
    found_node = linked_list.find(finding_value)
    if found_node is None:
        assert result is None
    else:
        assert found_node.value == result


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
def test_find(values, finding_value, result):
    linked_list = create_bidirect_linked_list(values)
    found_result = [node.value for node in linked_list.find_all(finding_value)]
    assert found_result == result
