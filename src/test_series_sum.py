"""Tests for series_sum.series_sum."""
import pytest


ASSERTIONS = [
    [0, "0.00"],
    [1, "1.00"],
    [2, "1.25"],
    [3, "1.39"]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_series_sum(n, result):
    """Test series_sum() for proper output in test cases."""
    from series_sum import series_sum
    assert series_sum(n) == result
