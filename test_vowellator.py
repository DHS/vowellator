import pytest
from vowellator import vowellate


@pytest.mark.parametrize("test_input,expected", [
    ("toller edwards aldrich", "aldrich edwards toller"),
])
def test_vowellator(test_input, expected):
    assert vowellate(test_input) == expected
