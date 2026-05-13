from calculator import add, sub, root

def test_add():
    assert add(2, 3) == 5
def test_sub():
    assert sub(10, 4) == 6

def test_root():
    assert root(4, 2) == 2
    assert root(3, 0) == None
    assert root(27, 3) == 0
