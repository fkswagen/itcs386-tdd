import pytest
from leap import is_leap

def test_2024_is_a_leap_year():
    assert is_leap(2024)

def test_1900_is_not_a_leap_year():
    assert not is_leap(1900)

@pytest.mark.parametrize("year, expected", [
    (2000, True),   # หาร 400 ลงตัว
    (1900, False),  # หาร 100 ลงตัว แต่หาร 400 ไม่ลงตัว
    (2024, True),   # หาร 4 ลงตัว แต่หาร 100 ไม่ลงตัว
    (2023, False),  # หาร 4 
    #เพิ่มเติม test case
    (2400, True),   
    (2100, False), 
])
def test_is_leap(year, expected):
    assert is_leap(year) == expected