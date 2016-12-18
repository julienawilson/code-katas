"""Tests for proper_parenthetics."""
import pytest


ASSERTIONS = [
    ['(', 1],
    ['(This is (a string)', 1],
    ['()', 0],
    ['some (strings) and (others)', 0],
    ['((Nestes)ones)', 0],
    [')', -1],
    ['(bloop))', -1],
    [')its backwards(', -1]
]


@pytest.mark.parametrize("input, result", ASSERTIONS)
def test_proper_parenthetics(input, result):
    """Test proper_parenthetics for proper output in test cases."""
    from proper_parenthetics import proper_parenthetics
    assert proper_parenthetics(input) == result
