from calculator import add, sub, divide

def test_add():
    assert add(2, 3) == 5
def test_sub():
    assert sub(10, 4) == 6

def test_divide():
    assert divide(4, 2) == 2
    assert divide(0, 5) == 0
