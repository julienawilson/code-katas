"""Tests for count_positives_sum_negatives.count_positives_sum_negatives."""
import pytest


ASSERTIONS = [
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], [10, -65]],
    [[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14], [8, -50]],
    [[1], [1, 0]],
    [[-1], [0, -1]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0]],
    [[], []]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_count_positives_sum_negatives(n, result):
    """Test count_positives_sum_negatives() for proper output in test cases."""
    from count_positives_sum_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives(n) == result
