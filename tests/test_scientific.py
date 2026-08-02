from core.scientific import ScientificEngine


def test_add():
    assert ScientificEngine.evaluate("2+3") == 5


def test_power():
    assert ScientificEngine.evaluate("2^5") == 32


def test_sqrt():
    assert ScientificEngine.evaluate("sqrt(25)") == 5


def test_pi():
    assert ScientificEngine.evaluate("sin(pi/2)") == 1.0


def test_division():
    assert ScientificEngine.evaluate("10/4") == 2.5


def test_negative():
    assert ScientificEngine.evaluate("-5+2") == -3


def test_parentheses():
    assert ScientificEngine.evaluate("(2+3)*4") == 20