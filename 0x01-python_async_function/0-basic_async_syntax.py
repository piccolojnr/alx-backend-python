#!/usr/bin/env python3
"""
module for wait_random
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    returns a random float between 0 and max_delay
    """
    random_number: float = random.random() * max_delay
    await asyncio.sleep(random_number)
    return random_number
