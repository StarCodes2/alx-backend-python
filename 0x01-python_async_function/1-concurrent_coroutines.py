#!/usr/bin/env python3
"""
    Defines an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay and spawns wait_random n times with
    the specified max_delay.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of the delay for each spawn. """
    if n < 1:
        return []
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    sorted_delays = []

    for delay in delays:
        append = True
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                append = False
                break
        if append:
            sorted_delays.append(delay)

    return sorted_delays
