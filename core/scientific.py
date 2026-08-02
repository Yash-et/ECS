"""
Scientific expression evaluator.
"""

from __future__ import annotations

from sympy import E, pi
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

from core.parser import ExpressionParser


class ScientificEngine:

    transformations = (
        standard_transformations
        + (implicit_multiplication_application,)
    )

    from sympy import (
    E,
    pi,
    sin,
    cos,
    tan,
    sqrt,
    log,
    exp,
    factorial,
    )

    LOCAL_DICT = {
        "pi": pi,
        "e": E,
        "sin": sin,
        "cos": cos,
        "tan": tan,
        "sqrt": sqrt,
        "log": log,
        "ln": log,
        "exp": exp,
        "factorial": factorial,
    }

    @classmethod
    def evaluate(cls, expression: str):
        expression = ExpressionParser.preprocess(expression)

        expr = parse_expr(
            expression,
            transformations=cls.transformations,
            local_dict=cls.LOCAL_DICT,
            evaluate=True,
        )

        if expr.is_Integer:
            return int(expr)
        if expr.is_Rational:
            return float(expr)
    
        return float(expr.evalf())