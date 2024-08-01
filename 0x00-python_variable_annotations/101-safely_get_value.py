#!/usr/bin/env python3
"""
    Defines a function that get a value with a specific key from a dictionary.
"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
  -> Union[Any, T]:
    """ Returns the a value from a dict using a specific key. """
    if key in dct:
        return dct[key]
    else:
        return default
