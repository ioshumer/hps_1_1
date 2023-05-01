import pytest

from source.powerset import PowerSet


def init_powerset(list_of_values):
    ps = PowerSet()
    for item in list_of_values:
        ps.put(item)
    return ps


@pytest.mark.parametrize(
    ("list_of_values"),
    [
        ([]),
        ([1]),
        ([1, 2]),
        ([1, 2, 3]),
        (list(range(100))),
    ]
)
def test_size_check(list_of_values):
    ps = PowerSet()
    for item in list_of_values:
        ps.put(item)

    assert ps.size() == len(list_of_values)
    if len(list_of_values):
        first_elem = list_of_values[0]
        ps.remove(first_elem)
        assert ps.size() == len(list_of_values) - 1

        for item in list_of_values:
            ps.remove(item)
        assert ps.size() == 0


@pytest.mark.parametrize(
    ("list_of_values"),
    [
        ([]),
        ([1]),
        ([1, 2]),
        ([1, 2, 3]),
        (list(range(100))),
    ]
)
def test_get(list_of_values):
    ps = PowerSet()
    for item in list_of_values:
        ps.put(item)

    for item in list_of_values:
        item_in_ps = ps.get(item)
        assert item_in_ps


@pytest.mark.parametrize(
    ("first_list", "second_list"),
    [
        ([], []),
        ([1, 2, 3], [2, 3, 4]),
        (list(range(0, 50)), list(range(25, 50)))
    ]
)
def test_intersection(first_list, second_list):
    ps1 = init_powerset(first_list)
    ps2 = init_powerset(second_list)
    ps = ps1.intersection(ps2)

    for elem in ps.data:
        assert (ps1.get(elem) and ps2.get(elem))

    for item in first_list:
        try:
            second_list.index(item)
        except BaseException as e:
            continue
        else:
            assert ps.get(item)


@pytest.mark.parametrize(
    ("first_list", "second_list"),
    [
        ([], []),
        ([1, 2, 3], [2, 3, 4]),
        (list(range(0, 50)), list(range(25, 50)))
    ]
)
def test_union(first_list, second_list):
    ps1 = init_powerset(first_list)
    ps2 = init_powerset(second_list)
    ps = ps1.union(ps2)

    for item in first_list:
        assert ps.get(item)

    for item in second_list:
        assert ps.get(item)


@pytest.mark.parametrize(
    ("first_list", "second_list"),
    [
        ([], []),
        ([1, 2, 3], [2, 3, 4]),
    ]
)
def test_diff(first_list, second_list):
    ps1 = init_powerset(first_list)
    ps2 = init_powerset(second_list)
    ps = ps1.difference(ps2)

    for elem in ps.data:
        assert (ps1.get(elem) is False or ps2.get(elem) is False)


@pytest.mark.parametrize(
    ("list_of_values", "list_for_subset", "bool_sign"),
    [
        ([], [], True),
        ([1], [1], True),
        ([1, 2], [1], True),
        ([1], [1, 2], False),
        (list(range(50)), [1, 2, 20], True),
    ]
)
def test_issubset(list_of_values, list_for_subset, bool_sign):
    ps = init_powerset(list_of_values)
    subset = init_powerset(list_for_subset)
    assert ps.issubset(subset) == bool_sign
