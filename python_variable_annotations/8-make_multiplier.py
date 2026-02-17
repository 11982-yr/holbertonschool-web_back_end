#!/usr/bin/env python3
"""Module that provides a type-annotated make_multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""

    def multiply(value: float) -> float:
        """Multiplies value by multiplier."""
        return value * multiplier

    return multiply
