import pytest
from dz14 import Rectangle


def test_perimeter():
    r = Rectangle(5, 10)
    assert r.perimeter() == 30


def test_area():
    r = Rectangle(5, 10)
    assert r.area() == 50


def test_add():
    r1 = Rectangle(5, 10)
    r2 = Rectangle(3, 7)
    r3 = r1 + r2
    assert r3.length == 8
    assert r3.width == 17


def test_subtract():
    r1 = Rectangle(5, 10)
    r2 = Rectangle(3, 7)
    r4 = r1 - r2
    assert r4.length == 2
    assert r4.width == 3


def test_str():
    r = Rectangle(5, 10)
    assert str(r) == 'Прямоугольник: Длина - 5, Ширина - 10'


if __name__ == '__main__':
    pytest.main()