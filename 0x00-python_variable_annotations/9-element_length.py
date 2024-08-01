#!/usr/bin/env python3

"""Duck typing an iterable/sequence"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Duck typing an iterable/sequence"""
    return [(i, len(i)) for i in lst]
