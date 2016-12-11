"""Tests for digitize.digitize."""
import pytest


ASSERTIONS = [
    [35231, [1, 3, 2, 5, 3]],
    [87, [7, 8]],
    [0, [0]],
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_digitize(n, result):
    """Test digitize() for proper output in test cases."""
    from digitize import digitize
    assert digitize(n) == result
