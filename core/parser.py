"""
Expression parser for the Engineering Calculator Suite.
"""

from __future__ import annotations

import re


class ExpressionParser:
    """
    Preprocess and validate mathematical expressions
    before SymPy evaluation.
    """

    REPLACEMENTS = {
        "×": "*",
        "÷": "/",
        "^": "**",
    }

    # Allows:
    # numbers
    # letters (function names: sin, cos, sqrt, etc.)
    # operators
    # brackets
    # decimal points
    # spaces
    ALLOWED_PATTERN = re.compile(
        r"^[0-9a-zA-Z_+\-*/().,%! ]+$"
    )

    @classmethod
    def preprocess(cls, expression: str) -> str:
        """
        Normalize and validate expression.
        """

        if not isinstance(expression, str):
            raise TypeError("Expression must be a string.")

        expression = expression.strip()

        if not expression:
            raise ValueError("Expression cannot be empty.")

        # Replace calculator symbols
        for old, new in cls.REPLACEMENTS.items():
            expression = expression.replace(old, new)

        # Security validation
        if not cls.ALLOWED_PATTERN.fullmatch(expression):
            raise ValueError(
                "Expression contains invalid characters."
            )

        return expression