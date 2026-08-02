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

    LOCAL_DICT = {
        "pi": pi,
        "e": E,
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

        return expr.evalf()