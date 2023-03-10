from simple_library_01.functions import add


def test_add():
    assert 4 == add(2, 2)

def test_add_not_equal():
    assert 28 + 72 == add(28, 72)

def test_add_with_zero():
    assert 12 == add(0, 12)

def test_add_negative():
    assert - 17 - 21 == add(-17, -21)

def test_add_pos_neg():
    assert -17 + 21 == add(-17, 21)

def test_add_floats():
    assert -17.25 + 21.01 == add(-17.25, 21.01)

