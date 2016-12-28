"""Tests for count_positives_sum_negatives.count_positives_sum_negatives."""
import pytest


ASSERTIONS = [
    [list('39A5T824Q7J6K'), list('A23456789TJQK')],
    [list('Q286JK395A47T'), list('A23456789TJQK')],
    [list('54TQKJ69327A8'), list('A23456789TJQK')],
    [list('AAA4555336773'), list('AAA3334555677')],
    [list('3'), list('3')],
    [list('TTTTTTTTTTTAK'), list('ATTTTTTTTTTTK')],
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_sort_cards(n, result):
    """Test sort_cards() for proper output in test cases."""
    from sort_cards import sort_cards
    assert sort_cards(n) == result


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_sort_cards_w_pq(n, result):
    """Test sort_cards_w_pq() for proper output in test cases."""
    from sort_cards import sort_cards
    assert sort_cards(n) == result
