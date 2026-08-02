"""
Expression parser for the Engineering Calculator Suite.
"""

from __future__ import annotations


class ExpressionParser:
    """Preprocess mathematical expressions before evaluation."""

    REPLACEMENTS = {
        "×": "*",
        "÷": "/",
        "^": "**",
    }

    @classmethod
    def preprocess(cls, expression: str) -> str:
        expression = expression.strip()

        for old, new in cls.REPLACEMENTS.items():
            expression = expression.replace(old, new)

        return expression