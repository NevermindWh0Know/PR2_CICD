from calculator import Calculator
import pytest

def test_add_first():
    calc = Calculator()
    assert calc.add(1, 1) == 2
