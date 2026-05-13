from calculator import add, sub, cosin
import math


def test_cosine():
    assert cosin(0) == 1
    assert cosin(math.pi / 2) == 0
    assert cosin(math.pi) == -1

