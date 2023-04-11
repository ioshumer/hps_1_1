import pytest

from source.ordered_list import OrderedList


@pytest.mark.parametrize(
    ('list_of_values', 'expected_array', 'length', 'asc'),
    [
        ([1], [1], 1, True),
        ([1, 2], [1, 2], 2, True),
        ([2, 1], [1, 2], 2, True),
        ([2, 1], [2, 1], 2, False),
        ([1, 2], [2, 1], 2, False),
        ([3, 2, 1], [1, 2, 3], 3, True),
        ([2, 1, 3], [1, 2, 3], 3, True),
        ([3, 1, 2], [1, 2, 3], 3, True),
        ([3, 2, 1], [3, 2, 1], 3, False),
        ([2, 1, 3], [3, 2, 1], 3, False),
        ([3, 1, 2], [3, 2, 1], 3, False),
    ]
)
def test_pop_on_empty(list_of_values, expected_array, length, asc):
    ol = OrderedList(asc)

    for i in list_of_values:
        ol.add(i)

    result = ol.get_all()

    assert expected_array == [i.value for i in result]
    assert length == ol.len()


@pytest.mark.parametrize(
    ('list_of_values', 'value_to_delete', 'expected_array', 'length', 'asc'),
    [
        ([1], 1, [], 0, True),
        ([1], 2, [1], 1, True),
        ([1, 2], 2, [1], 1, True),
        ([2, 1], 2, [1], 1, True),
        ([1, 2, 3], 2, [1, 3], 2, True),
        ([3, 2, 1], 2, [1, 3], 2, True),
    ]
)
def test_delete(list_of_values, value_to_delete, expected_array, length, asc):
    ol = OrderedList(asc)

    for i in list_of_values:
        ol.add(i)

    ol.delete(value_to_delete)

    result = ol.get_all()
    assert expected_array == [i.value for i in result]
    assert length == ol.len()