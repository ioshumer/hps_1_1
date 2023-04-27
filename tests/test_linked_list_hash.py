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