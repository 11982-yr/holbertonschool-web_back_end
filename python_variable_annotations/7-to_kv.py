#!/usr/bin/env python3
"""Module that provides a type-annotated to_kv function."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string and the square of the number as a float."""
    return (k, float(v ** 2))
