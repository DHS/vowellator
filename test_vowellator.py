
from vowellator import vowellate, read_csv

def test_vowellator():
    assert vowellate("toller edwards aldrich") == "aldrich edwards toller"


def test_csv_reader():
    name_list = read_csv()
    assert name_list == "steph dave tosin debbie tagazzu"