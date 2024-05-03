#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

"""Let's duck type an iterable object"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Let's duck type an iterable object"""
    return [(i, len(i)) for i in lst]
