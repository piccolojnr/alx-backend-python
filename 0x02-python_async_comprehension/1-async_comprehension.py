#!/usr/bin/env python3
"""
Asyncio module
"""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> list:
    """
    Async comprehension
    """
    return [i async for i in async_generator()]
