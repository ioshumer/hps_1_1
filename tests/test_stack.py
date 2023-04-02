import pytest

from source.stack import Stack


@pytest.mark.parametrize(
    ('exptected_value'),
    [
        (None),
    ]
)
def test_pop_on_empty(exptected_value):
    """

    :param exptected_value:
    :return:
    """
    stack = Stack()
    value = stack.pop()
    assert value == exptected_value


@pytest.mark.parametrize(
    ('given_input_array', 'expected_output_array'),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
    ]
)
def test_stack_work(given_input_array, expected_output_array):
    stack = Stack()
    for value in given_input_array:
        stack.push(value)

    output_array = []
    while stack.size() > 0:
        value = stack.pop()
        output_array.append(value)

    assert output_array == expected_output_array


@pytest.mark.parametrize(
    ('input_array', 'expected_stack_size'),
    [
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 3),
        (list(range(1000)), 1000)
    ]
)
def test_stack_size(input_array, expected_stack_size):
    stack = Stack()
    for value in input_array:
        stack.push(value)

    assert stack.size() == expected_stack_size


@pytest.mark.parametrize(
    ('initial_array', 'additional_item', 'final_stack_size', 'final_array'),
    [
        ([1], 2, 2, [2, 1]),
    ]
)
def test_push(initial_array, additional_item, final_stack_size, final_array):
    stack = Stack()
    for value in initial_array:
        stack.push(value)
    stack.push(additional_item)

    assert stack.size() == final_stack_size

    stack_output = []
    while stack.size() > 0:
        value = stack.pop()
        stack_output.append(value)

    assert stack_output == final_array
    assert stack.size() == 0
