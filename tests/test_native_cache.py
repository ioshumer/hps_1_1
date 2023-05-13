from source.native_cache import NativeCache


def test_amount_of_hits():
    nc = NativeCache(3)
    key_values = [
        [0, 'a'],
        [1, 'b'],
        [2, 'c']
    ]
    for key, value in key_values:
        nc.put(key, value)

    get_amount = 5
    key = 0
    key_idx = nc.find_key_idx(key)

    for _ in range(get_amount):
        nc.get(key)

    assert nc.hits[key_idx] == get_amount


def test_collisions_resolve():
    key_to_remove = 2

    nc = NativeCache(3)
    nc.put(0, 'a')
    nc.put(1, 'b')
    nc.put(key_to_remove, 'c')

    key_to_remove_idx = nc.find_key_idx(key_to_remove)

    nc.get(0)
    nc.get(1)

    new_key = 3
    new_value = "hello"
    nc.put(new_key, new_value)

    new_key_idx = nc.find_key_idx(new_key)

    assert key_to_remove_idx == new_key_idx
