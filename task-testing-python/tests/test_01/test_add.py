from simple_library_01.functions import add


def test_add():
    assert 4 == add(2, 2)
    assert 100 == add(28, 72)
    assert 12 == add(0, 12)
    assert -43 == add(-10, -33)

