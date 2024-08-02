#!/usr/bin/env python3

"""Duck typing a general input and output"""

from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Takes in a sequence with elements of any type, and returns either
    an element of that sequence, or None"""
    if lst:
        return lst[0]
    else:
        return None
