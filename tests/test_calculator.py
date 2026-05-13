from calculator import (
    add, sub, root, square, multiply, divide, cosin, factorial, sinus
)
import math


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(4, 2) == 2
    assert divide(0, 5) == 0


def test_root():
    assert root(4, 2) == 2
    assert root(3, 0) is None
    assert root(27, 3) == 3


def test_square():
    assert square(2, 3) == 8


def test_cosine():
    assert cosin(0) == 1
    # Use round() to handle floating-point precision issues
    assert round(cosin(math.pi / 2), 5) == 0
    assert cosin(math.pi) == -1


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_sinus():
    assert sinus(0) == 0
    assert round(sinus(math.pi / 2), 5) == 1
