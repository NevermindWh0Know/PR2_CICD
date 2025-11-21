from calculator import Calculator
import pytest

def test_add_method_exists():
    calc = Calculator()
    assert hasattr(calc, 'add')
