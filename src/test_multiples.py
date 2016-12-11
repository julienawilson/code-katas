"""Tests for multiples.multiples."""
import pytest


ASSERTIONS = [
    [2, 4, 40, [4, 8, 12, 16, 20, 24, 28, 32, 36]],
    [3, 4, 40, [12, 24, 36]],
    [7, 4, 80, [28, 56]],
    [7, 4, 20, []]
]


@pytest.mark.parametrize("s1, s2, s3, result", ASSERTIONS)
def test_multiples(s1, s2, s3, result):
    """Test multiples() for proper output in test cases."""
    from multiples import multiples
    assert multiples(s1, s2, s3) == result
