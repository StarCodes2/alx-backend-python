#!/usr/bin/env python3
"""
    Defines a function that returns a List of Tuples of sequences
    and thier length.
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a List of Tuples. """
    return [(i, len(i)) for i in lst]
