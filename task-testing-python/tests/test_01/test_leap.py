from simple_library_01.functions import is_leap
import pytest


def test_leap():
    assert True == is_leap(1984)
    assert False == is_leap(1800)
    assert True == is_leap(1600)
    assert False == is_leap(1999)


def test_leap_with_exception():
    try:
        is_leap(-1)
        assert False
    except AttributeError:
        assert True
