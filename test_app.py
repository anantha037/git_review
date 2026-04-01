from app import add, mulitply, substract

def test_app():
    assert add(2, 5) == 7

def test_multiply():
    assert mulitply(10, 2) == 20


def test_substract():
    assert substract(10,3) == 7