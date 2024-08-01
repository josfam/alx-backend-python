#!/usr/bin/env python3

"""A type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
"""

from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as argument and returns a function that
    multiplies a float by multiplier.
    """
    def float_multiplier(num: float) -> float:
        return num * multiplier

    return float_multiplier
