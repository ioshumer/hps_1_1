import pytest

from source.twoway_queue import TwoWayQueue, Node


@pytest.mark.parametrize(
    ('list_of_values', 'exptected_array', 'size'),
    [
        ([], [], 0),
        ([1], [1], 1),
        ([1, 2], [1, 2], 2),
        ([1, 2, 3], [1, 2, 3], 3),
    ]
)
def test_add_front_remove_tail(list_of_values, exptected_array, size):
    queue = TwoWayQueue()
    for item in list_of_values:
        queue.addFront(item)
    assert queue.size() == size

    real_array = []
    while queue.size() > 0:
        value = queue.removeTail()
        real_array.append(value)

    assert real_array == exptected_array
    assert queue.size() == 0


@pytest.mark.parametrize(
    ('list_of_values', 'exptected_array', 'size'),
    [
        ([], [], 0),
        ([1], [1], 1),
        ([1, 2], [1, 2], 2),
        ([1, 2, 3], [1, 2, 3], 3),
    ]
)
def test_add_tail_remove_front(list_of_values, exptected_array, size):
    queue = TwoWayQueue()
    for item in list_of_values:
        queue.addFront(item)
    assert queue.size() == size

    real_array = []
    while queue.size() > 0:
        value = queue.removeTail()
        real_array.append(value)

    assert real_array == exptected_array
    assert queue.size() == 0


@pytest.mark.parametrize(
    ('list_of_values', 'exptected_array', 'size'),
    [
        ([], [], 0),
        ([1], [1], 1),
        ([1, 2], [2, 1], 2),
        ([1, 2, 3], [3, 2, 1], 3),
    ]
)
def test_add_front_remove_front(list_of_values, exptected_array, size):
    queue = TwoWayQueue()
    for item in list_of_values:
        queue.addFront(item)
    assert queue.size() == size

    real_array = []
    while queue.size() > 0:
        value = queue.removeFront()
        real_array.append(value)

    assert real_array == exptected_array
    assert queue.size() == 0


@pytest.mark.parametrize(
    ('list_of_values', 'exptected_array', 'size'),
    [
        ([], [], 0),
        ([1], [1], 1),
        ([1, 2], [2, 1], 2),
        ([1, 2, 3], [3, 2, 1], 3),
    ]
)
def test_add_tail_remove_tail(list_of_values, exptected_array, size):
    queue = TwoWayQueue()
    for item in list_of_values:
        queue.addTail(item)
    assert queue.size() == size

    real_array = []
    while queue.size() > 0:
        value = queue.removeTail()
        real_array.append(value)

    assert real_array == exptected_array
    assert queue.size() == 0
