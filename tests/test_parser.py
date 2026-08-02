from core.parser import ExpressionParser


def test_replace_symbols():

    assert ExpressionParser.preprocess("2×3") == "2*3"

    assert ExpressionParser.preprocess("8÷2") == "8/2"

    assert ExpressionParser.preprocess("2^5") == "2**5"