#!/usr/bin/python3
"""Module for safely_get_value function"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
  dct: Mapping,
  key: Any,
  default: Union[T, None] = None
) -> Union[Any, T]
"""Return the value for key in dct if present, otherwise default"""
    if key in dct:
        return dct[key]
    else:
        return default
