#!/usr/bin/env python3
"""
    Defines a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies its argument by multiplier. """
    def return_function(value: float):
        """ Returns value multiplied by multiplier. """
        return value * multiplier
    return return_function
