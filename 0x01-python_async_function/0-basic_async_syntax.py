#!/usr/bin/env python3
"""
    Defines an asynchronous coroutine that takes in an int argument (max_delay)
    and waits for a random delay between 0 and max_delay
"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a specicied amount of seconds. """
    if max_delay < 1:
        delay: int = 0
    else:
        delay: int = random.uniform(0, max_delay)
    now: float = time.perf_counter()
    await asyncio.sleep(delay)

    return (time.perf_counter() - now)
