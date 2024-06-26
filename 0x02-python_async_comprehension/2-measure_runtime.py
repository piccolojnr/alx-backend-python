#!/usr/bin/env python3
"""
Asyncio module
"""
import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_generator


async def measure_runtime() -> float:
    """
    measure_runtime - measures the total runtime
    """
    start = time.time()
    await asyncio.gather(*(await async_comprehension() for _ in range(4)))
    return time.time() - start
