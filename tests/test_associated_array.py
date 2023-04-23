import pytest

from source.associated_array import NativeDictionary


@pytest.mark.parametrize(
    ("size", "key", "value", "new_value"),
    [
        (127, 'hello', 'world', 'amigo'),
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


def test_get():
    key = "hello"
    value = "world"

    nd = NativeDictionary(17)
    nd.put(key, value)
    assert nd.get(key) == value
    assert nd.get("non_existed") is None


def test_is_key():
    key = "hello"
    value = "world"

    nd = NativeDictionary(17)
    nd.put(key, value)
    assert nd.is_key(key) is True
    assert nd.is_key("non_existed") is False

@pytest.mark.parametrize(
    ("size", "key", "value"),
    [
        (7, "a", 100),
    ]
)
def test_put_on_new_key(size, key, value):
    nd = NativeDictionary(size)
    nd.put(key, value)

    assert nd.get(key) == value
