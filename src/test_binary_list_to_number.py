"""Tests for binary_list_to_number.binary_list_to_number."""
import pytest


ASSERTIONS = [
    [[0, 0, 0, 1], 1],
    [[0, 0, 1, 0], 2],
    [[1, 1, 1, 1], 15],
    [[0, 1, 1, 0], 6]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_binary_list_to_number(n, result):
    """Test binary_list_to_number() for proper output in test cases."""
    from binary_list_to_number import binary_list_to_number
    assert binary_list_to_number(n) == result
