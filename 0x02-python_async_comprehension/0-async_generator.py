#!/usr/bin/env python3
"""
    Defines an async coroutine that loops 10 times and yields a random number
    between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yields a random numbers between 0 and 10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
