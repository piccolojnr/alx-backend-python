#!/usr/bin/env python3
"""
measure_time - measures the total execution time for wait_n
"""

import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time - measures the total execution time for wait_n
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()
    return (end - start) / n
