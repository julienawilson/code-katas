"""Tests for reverse_and_mirror.reverse_and_mirror."""
import pytest


ASSERTIONS = [
    ["FizZ", "buZZ", "zzUB@@@zZIffIZz"],
    ["String Reversing", "Changing Case", "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING"] 
]


@pytest.mark.parametrize("s1, s2, result", ASSERTIONS)
def test_reverse_and_mirror(s1, s2, result):
    """Test reverse_and_mirror() for proper output in test cases."""
    from reverse_and_mirror import reverse_and_mirror
    assert reverse_and_mirror(s1, s2) == result
