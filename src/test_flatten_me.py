"""Tests for flatten_me.flatten_me."""
import pytest


ASSERTIONS = [
    [[1, [2, 3], 4], [1, 2, 3, 4]],
    [[['a', 'b'], 'c', ['d']], ['a', 'b', 'c', 'd']],
    [['!', '?'], ['!', '?']],
    [[[True, False], ['!'], ['?'], [71, '@']], [True, False, '!', '?', 71, '@']]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_flatten_me(n, result):
    """Test flatten_me() for proper output in test cases."""
    from flatten_me import flatten_me
    assert flatten_me(n) == result
