#!/usr/bin/env python3
from typing import Callable

"""Complex types - functions"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Complex types - functions"""

    def multiplier_function(x: float) -> float:
        """Complex types - functions"""

        return x * multiplier

    return multiplier_function
