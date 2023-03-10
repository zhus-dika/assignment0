from simple_library_01.functions import *


def test_get_month_days():
    for i in range(1, 13):
        assert 30 == get_month_days(1930, i)
    for i in [2000, 2012, 2023, 2200]:
        for j in [4, 6, 9, 11]:
            assert 30 == get_month_days(i, j)
        for j in [1, 3, 5, 7, 8, 10, 12]:
            assert 31 == get_month_days(i, j)
        if is_leap(i):
            assert 29 == get_month_days(i, 2)
        else:
            assert 28 == get_month_days(i, 2)


def test_get_month_days_with_exception():
    try:
        get_month_days(1, 22)
        assert False
    except AttributeError:
        assert True

