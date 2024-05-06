#!/usr/bin/env python3
"""
A coroutine that takes in an integer max_delay and returns a list of
random delay values between 0 and max_delay with asyncio.
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for n tasks to complete, with a maximum delay between each task.
    """
    delays = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delays)
