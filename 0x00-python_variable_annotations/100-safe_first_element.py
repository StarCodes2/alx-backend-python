#!/usr/bin/env python3
"""
    Defines a duck-typed annotated function that returns the value of
    its argument first element.
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
