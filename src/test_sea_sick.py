"""Tests for sea_sick.sea_sick."""
import pytest


ASSERTIONS = [
    ["~", "No Problem"],
    ["_~~~~~~~_~__~______~~__~~_~~", "Throw Up"],
    ["______~___~_", "Throw Up"],
    ["____", "No Problem"],
    ["_~~_~____~~~~~~~__~_~", "Throw Up"]
]


@pytest.mark.parametrize("n, result", ASSERTIONS)
def test_sea_sick(n, result):
    """Test sea_sick() for proper output in test cases."""
    from sea_sick import sea_sick
    assert sea_sick(n) == result
