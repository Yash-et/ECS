from core.scientific import ScientificEngine


def test_sin():
    assert ScientificEngine.evaluate("sin(pi/2)") == 1.0


def test_cos():
    assert ScientificEngine.evaluate("cos(0)") == 1.0


def test_log():
    assert ScientificEngine.evaluate("log(100,10)") == 2.0


def test_factorial():
    assert ScientificEngine.evaluate("factorial(5)") == 120


def test_exp():
    assert round(
        ScientificEngine.evaluate("exp(2)"),
        5,
    ) == 7.38906