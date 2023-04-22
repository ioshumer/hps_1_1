import pytest

from source.associated_array import NativeDictionary


@pytest.mark.parametrize(
    ("size", "key", "value", "new_value"),
    [
        (127, 'hello', 'world', 'amigo')
    ]
)
def test_native_dictonary(size, key, value, new_value):
    nd = NativeDictionary(size)
    nd.put(key, value)

    saved_value = nd.get(key)

    assert nd.is_key(key) is True
    assert saved_value == value

    nd.put(key, new_value)
    another_value = nd.get(key)

    assert nd.is_key(key) is True
    assert another_value == new_value

    assert nd.is_key('capibara') is False
    assert nd.get('capibara') is None
