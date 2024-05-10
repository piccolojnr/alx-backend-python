#!/usr/bin/env python3
"""
Asyncio module
"""
import typing

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Async comprehension
    """
    return [i async for i in async_generator()]
