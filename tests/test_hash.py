import pytest

from source.hash_tables import HashTable


@pytest.mark.parametrize(
    ('size', 'step', 'list_of_values', 'expected_slots_list', 'finding_value', 'finded_slot'),
    [
        (5, 1, [1], [None, None, None, None, '1'], 1, 4),
        (5, 1, [1, 1], ['1', None, None, None, '1'], 1, 0),
        (5, 1, [1, 1, 1], ['1', '1', None, None, '1'], 1, 0),
        (5, 1, [1, 1, 1, 1], ['1', '1', '1', None, '1'], 1, 0),
        (5, 1, [1, 1, 1, 1, 1], ['1', '1', '1', '1', '1'], 1, 0),
        (5, 1, [4, 4], [None, None, '4', '4', None], 4, 2),
        (17, 3, [1, 2, 3, 4, 5], ['3', '4', '5'] + [None] * 12 + ['1', '2'], 3, 0),
        (17, 3, [1, 2, 3, 4, 5], ['3', '4', '5'] + [None] * 12 + ['1', '2'], 2, 16),
    ]
)
def test_hash_slots(size, step, list_of_values, expected_slots_list, finding_value, finded_slot):
    ht = HashTable(size, step)
    for i in list_of_values:
        ht.put(str(i))

    assert ht.slots == expected_slots_list
    assert ht.find(str(finding_value)) == finded_slot
