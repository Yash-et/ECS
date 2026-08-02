"""
Scientific expression evaluator.
"""

from __future__ import annotations

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

from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

from core.parser import ExpressionParser


class ScientificEngine:
    """
    Scientific calculator engine using SymPy.
    """

    transformations = (
        standard_transformations
        + (implicit_multiplication_application,)
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
        """
        Evaluate mathematical expression.
        """

        expression = ExpressionParser.preprocess(
            expression
        )

        try:
            expr = parse_expr(
                expression,
                local_dict=cls.LOCAL_DICT,
                transformations=cls.transformations,
                evaluate=True,
            )

        except Exception as exc:
            raise ValueError(
                f"Invalid expression: {exc}"
            )

        if expr.is_Integer:
            return int(expr)

        if expr.is_Rational:
            return float(expr)

        return float(expr.evalf())