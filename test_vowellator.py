import pytest
from vowellator import vowellate


@pytest.mark.parametrize("test_input,expected", [
    ("toller edwards aldrich", "aldrich edwards toller"),
    ("button gregory raley", "raley gregory button"),
])
def test_vowellator(test_input, expected):
    assert vowellate(test_input) == expected
