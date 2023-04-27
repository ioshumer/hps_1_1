import pytest

from source.linked_list_hash import HashTable


@pytest.mark.parametrize(
    ('size', 'values', 'found_values'),
    [
        (5, [1], [1]),
        (5, [1, 2], [1, 2]),
        (5, [1, 2, 3], [1, 2, 3]),
        (5, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        # (5, 1, [1, 1], ['1', None, None, None, '1'], 1, 0),
        # (5, 1, [1, 1, 1], ['1', '1', None, None, '1'], 1, 0),
        # (5, 1, [1, 1, 1, 1], ['1', '1', '1', None, '1'], 1, 0),
        # (5, 1, [1, 1, 1, 1, 1], ['1', '1', '1', '1', '1'], 1, 0),
        # (5, 1, [4, 4], [None, None, '4', '4', None], 4, 2),
        # (17, 3, [1, 2, 3, 4, 5], ['3', '4', '5'] + [None] * 12 + ['1', '2'], 3, 0),
        # (17, 3, [1, 2, 3, 4, 5], ['3', '4', '5'] + [None] * 12 + ['1', '2'], 2, 16),
    ]
)
def test_hash_slots(size, values, found_values):
    ht = HashTable(size)
    for i in values:
        ht.put(i)

    results_list = []
    for value in values:
        value = str(value)
        idx = ht.find(value)
        linked_list = ht.slots[idx]
        node = linked_list.head
        while node is not None:
            if node.value == value:
                results_list.append(node.value)
                assert node.value == value
            node = node.next
    assert found_values == results_list
    # assert ht.slots == expected_slots_list
    # assert ht.find(str(finding_value)) == finded_slot
