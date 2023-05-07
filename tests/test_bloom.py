import pytest

from source.bloom_filter import BloomFilter


@pytest.mark.parametrize(
    ("input", "output"),
    [
        ("hello", 4),
    ]
)
def test_hash1(input, output):
    bf = BloomFilter(32)
    assert bf.hash1(input) == output


def test_bloom():
    bf = BloomFilter(32)
    bf.add("hello")
    assert bf.is_value("hello") is True
    assert bf.is_value("hello, world") is False
