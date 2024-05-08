#!/usr/bin/env python3
import asyncio
import time

"""
Asyncio module
"""


async_comprehension = __import__("1-async_comprehension").async_generator


async def measure_runtime() -> float:
    """
    measure_runtime - measures the total runtime
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
