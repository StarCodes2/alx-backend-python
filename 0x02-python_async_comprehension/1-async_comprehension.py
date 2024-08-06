#!/usr/bin/env python3
"""
    Defines an async coroutine that collects 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        Uses an async comprehensing over async_generator and return
        a list of 10 float.
    """
    return [i async for i in async_generator()]
