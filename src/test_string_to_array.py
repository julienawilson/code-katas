"""Tests for string_to_array.string_to_array."""
import pytest


ASSERTIONS = [
    ["Robin Singh", ["Robin", "Singh"]],
    ["CodeWars", ["CodeWars"]],
    ["I love arrays they are my favorite", ["I", "love", "arrays", "they", "are", "my", "favorite"]],
    ["1 2 3", ["1", "2", "3"]],
    ["", [""]]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_string_to_array(n, result):
    """Test string_to_array() for proper output in test cases."""
    from string_to_array import string_to_array
    assert string_to_array(n) == result
