#!/usr/bin/env python3
"""
    Defines an asynchronous coroutine that takes in an int argument (max_delay)
    and waits for a random delay between 0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a specicied amount of seconds. """
    if max_delay < 1:
        delay: float = 0.0
    else:
        delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
