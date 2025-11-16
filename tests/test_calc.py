from calculator import Calculator
import pytest

def test_add_first():
    calc = Calculator()
    assert calc.add(1, 1) == 2

def test_add_second():
    calc = Calculator()
    assert calc.add(2, 2) == 4

def test_sub_third():
    calc = Calculator()
    assert calc.sub(5, 3) == 2
