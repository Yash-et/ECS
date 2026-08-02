from core.scientific import ScientificEngine


def test_add():

    assert ScientificEngine.evaluate("2+3") == 5


def test_power():

    assert ScientificEngine.evaluate("2^5") == 32


def test_sqrt():

    assert ScientificEngine.evaluate("sqrt(25)") == 5


def test_pi():

    result = ScientificEngine.evaluate("sin(pi/2)")

    assert round(float(result), 5) == 1.0