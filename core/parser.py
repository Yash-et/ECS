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
    FORBIDDEN = [
        "__",
        "import",
        "exec",
        "eval",
        "lambda",
        "os",
        "sys",
        "subprocess",
    ]
    @classmethod
    def preprocess(cls, expression: str) -> str:
        expression = expression.strip()

        for old, new in cls.REPLACEMENTS.items():
            expression = expression.replace(old, new)
            
        for word in cls.FORBIDDEN:
            if word in expression:
                raise ValueError(f"Illegal token: {word}")
        return expression        