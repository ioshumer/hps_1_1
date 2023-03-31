import pytest

from source.dynamic_array import DynArray


@pytest.mark.parametrize(
    ('array_values', 'length', 'first', 'last', 'capacity'),
    [
        ([1], 1, 1, 1, 16,),
        ([1, 2], 2, 1, 2, 16),
        ([1, 2, 3], 3, 1, 3, 16),
        (list(range(17)), 17, 0, 16, 32)
    ]
)
def test_append(array_values, length, first, last, capacity):
    dyn_arr = DynArray()
    for item in array_values:
        dyn_arr.append(item)

    assert len(dyn_arr) == length
    assert dyn_arr[0] == first
    assert dyn_arr[len(dyn_arr) - 1] == last
    assert dyn_arr.capacity == capacity


@pytest.mark.parametrize(
    ('array_values', 'final_capacity', 'inserting_idx', 'inserting_value', 'final_array'),
    [
        ([], 16, 0, 1, [1]),                                                    # вставка в пустой массив
        ([2], 16, 0, 1, [1, 2]),                                                # вставка первым
        ([1], 16, 1, 2, [1, 2]),                                                # вставка вторым
        ([1, 3], 16, 1, 2, [1, 2, 3]),                                          # вставка в середину
        ([i for i in range(15)], 16, 15, 100, [i for i in range(15)]+[100]),    # вставка крайнего до увеличения
        ([i for i in range(16)], 32, 16, 100, [i for i in range(16)]+[100]),    # вставка с увеличением capacity
        ([i for i in range(16)], 32, 17, 100, [i for i in range(16)]+[100]),    # вставка в недопустимую позицию
        ([i for i in range(16)], 32, -1, 100, [i for i in range(16)]+[100]),    # вставка в недопустимую позицию
    ]
)
def test_insert(array_values, final_capacity, inserting_idx, inserting_value, final_array):
    dyn_arr = DynArray()
    for item in array_values:
        dyn_arr.append(item)

    if inserting_idx < 0 or inserting_idx > dyn_arr.count:
        with pytest.raises(IndexError):
            dyn_arr.insert(inserting_idx, inserting_value)
        return

    dyn_arr.insert(inserting_idx, inserting_value)
    assert dyn_arr.capacity == final_capacity
    assert dyn_arr[inserting_idx] == inserting_value
    assert dyn_arr.as_list() == final_array


testing_args = (
    'initial_array', 'final_array',
    'deleted_idx',
    'initial_capacity',  'initial_counter',
    'final_capacity','final_counter',
)


def get_dynamic_array_from_list(array_values):
    dyn_arr = DynArray()
    for value in array_values:
        dyn_arr.append(value)
    return dyn_arr


@pytest.mark.parametrize(
    testing_args,
    [
        ([], 1, 16, 16, 0, 0, []),
    ]
)
def test_delete_on_incorrect_index(initial_array, final_array, deleted_idx,
                                   initial_capacity, initial_counter, final_capacity, final_counter):
    """Попытка удаления элемента в недопустимой позиции"""
    dyn_arr = get_dynamic_array_from_list(initial_array)



    if deleted_idx >= len(dyn_arr):
        with pytest.raises(IndexError):
            dyn_arr.delete(deleted_idx)

@pytest.mark.parametrize(
    (),
    [
        ([], 1, 16, 16, 0, 0, []),
    ]
)
def test_delete(array_values, deleted_idx, initial_capacity, final_capacity, initial_counter, final_counter, final_array):
    dyn_arr = get_dynamic_array_from_list(array_values)

    if deleted_idx >= len(dyn_arr):
        with pytest.raises(IndexError):
            dyn_arr.delete(deleted_idx)
    #     return
    #
    # assert dyn_arr.capacity == initial_capacity
    # assert dyn_arr.count == initial_counter
    #
    # dyn_arr.delete(deleted_idx)
    #
    # assert dyn_arr.capacity == final_capacity
    # assert dyn_arr.count == final_counter
    # assert dyn_arr.as_list() == final_array
