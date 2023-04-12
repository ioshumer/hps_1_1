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
        ([6, 1, 4, 2, 0, 3, 8, 9, 7, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10, True)
    ]
)
def test_pop_on_empty(list_of_values, expected_array, length, asc):
    ol = OrderedList(asc)

    for i in list_of_values:
        ol.add(i)

    forward_result = ol.get_all()
    list_items = [i.value for i in forward_result]
    assert list_items == expected_array

    backward_result = ol.get_all(False)
    list_items = [i.value for i in backward_result]
    assert list_items == expected_array[::-1]

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


@pytest.mark.parametrize(
    ('list_of_values', 'value_to_find', 'expected_value', 'asc'),
    [
        ([1, 2, 3], 3, 3, True)
    ]
)
def test_find(list_of_values, value_to_find, expected_value, asc):
    ol = OrderedList(asc)

    for i in list_of_values:
        ol.add(i)

    finded = ol.find(value_to_find)

    assert (finded.value if finded else None) == expected_value
