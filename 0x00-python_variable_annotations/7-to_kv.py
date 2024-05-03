#!/usr/bin/env python3
from typing import Union, Tuple

"""Complex types - string and int/float to tuple"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Complex types - string and int/float to tuple"""
    return (k, v * v)
