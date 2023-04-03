import pytest

from source.queue import Queue


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
    queue = Queue()
    value = queue.dequeue()
    assert value == exptected_value


@pytest.mark.parametrize(
    ('given_input_array', 'expected_output_array'),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
    ]
)
def test_queue_work(given_input_array, expected_output_array):
    queue = Queue()
    for value in given_input_array:
        queue.enqueue(value)

    output_array = []
    while queue.size() > 0:
        value = queue.dequeue()
        output_array.append(value)

    assert output_array == expected_output_array


@pytest.mark.parametrize(
    ('input_array', 'expected_queue_size'),
    [
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 3),
        (list(range(1000)), 1000)
    ]
)
def test_stack_size(input_array, expected_queue_size):
    queue = Queue()
    for value in input_array:
        queue.enqueue(value)

    assert queue.size() == expected_queue_size


@pytest.mark.parametrize(
    ('initial_array', 'additional_item', 'final_queue_size', 'final_array'),
    [
        ([1], 2, 2, [1, 2]),
        ([1, 2], 2, 3, [1, 2, 2]),
    ]
)
def test_enqueue(initial_array, additional_item, final_queue_size, final_array):
    queue = Queue()
    for value in initial_array:
        queue.enqueue(value)
    queue.enqueue(additional_item)

    assert queue.size() == final_queue_size

    stack_output = []
    while queue.size() > 0:
        value = queue.dequeue()
        stack_output.append(value)

    assert stack_output == final_array
    assert queue.size() == 0
