
from core.arithmetic import ArithmeticEngine


def test_add():
    assert ArithmeticEngine.add(5, 2) == 7


def test_subtract():
    assert ArithmeticEngine.subtract(5, 2) == 3


def test_multiply():
    assert ArithmeticEngine.multiply(5, 2) == 10


def test_divide():
    assert ArithmeticEngine.divide(10, 2) == 5