import pytest

from source.hash_tables import HashTable


@pytest.mark.parametrize(
    ('size', 'step', 'list_of_values', 'expected_slots_list'),
    [
        (5, 1, [1], [None, None, None, None, '1']),
        (5, 1, [1, 1], ['1', None, None, None, '1']),
        (5, 1, [1, 1, 1], ['1', '1', None, None, '1']),
        (5, 1, [1, 1, 1, 1], ['1', '1', '1', None, '1']),
        (5, 1, [1, 1, 1, 1, 1], ['1', '1', '1', '1', '1']),
        (5, 1, [4, 4], [None, None, '4', '4', None]),
        # (5, 1, [0, 1, 2, 3, 4], ['0', '1', '2', '3', '4']),
    ]
)
def test_hash_slots(size, step, list_of_values, expected_slots_list):
    ht = HashTable(size, step)
    for i in list_of_values:
        ht.put(str(i))

    assert ht.slots == expected_slots_list
