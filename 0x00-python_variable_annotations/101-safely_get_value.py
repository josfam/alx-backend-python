#!/usr/bin/env python3

"""Complex type annotations with TypeVar"""

from typing import Any, Union, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Takes a mapping, a key, and a default value.
    Returns the value of the key, or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
