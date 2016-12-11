"""Tests for last.last."""
import pytest


ASSERTIONS = [
    [[1, 2, 3, 4, 5], 5],
    ["abcde", "e"],
    [(1, "b", 3, "d", 5), 5],
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_last(n, result):
    """Test last() for proper output in test cases ASSERTIONS."""
    from last import last
    assert last(n) == result
