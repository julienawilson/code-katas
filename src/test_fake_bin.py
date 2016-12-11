"""Tests for fake_bin.fake_bin."""
import pytest


ASSERTIONS = [
    ["45385593107843568", "01011110001100111"],
    ["509321967506747", "101000111101101"],
    ["366058562030849490134388085", "011011110000101010000011011"],
    ["15889923", "01111100"],
    ["800857237867", "100111001111"]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_fake_bin(n, result):
    """Test fake_bin() for proper output in test cases."""
    from fake_bin import fake_bin
    assert fake_bin(n) == result
