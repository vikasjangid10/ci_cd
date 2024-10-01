from src.operations import add , sub

def test_add():
    assert add(2,2) == 4
    assert add(4,6) == 10

def test_sub():
    assert sub(5,2) == 3
    assert sub(6,1) == 5
    assert sub(98,8) == 90
    assert sub(5,4) == 1