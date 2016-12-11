"""Tests for sum_from_string.sum_from_string."""
import pytest


ASSERTIONS = [
    ["In 2015, I want to know how much does iPhone 6+ cost?", 2021],
    ["1+1=2", 4],
    ["e=mc^2", 2],
    ["seventy two", 0],
    ["7.2", 9]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_sum_from_string(n, result):
    """Test sum_from_string() for proper output in test cases."""
    from sum_from_string import sum_from_string
    assert sum_from_string(n) == result
