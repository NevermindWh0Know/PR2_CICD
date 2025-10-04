from calculator import add, sub, mul, div
import pytest

def test_add():
    assert calc.add(2, 3) == 5

def test_sub():
    assert calc.sub(5, 3) == 2

def test_mul():
    assert calc.mul(4, 3) == 12

def test_div():
    assert calc.div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        calc.div(1, 0)
