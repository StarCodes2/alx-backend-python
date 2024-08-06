#!/usr/bin/env python3
"""
    Defines an async coroutine that executes async_comprehension four times
    in parallel using asyncio.gather.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the time it takes to execute async_comprehension 4 times """
    start = time.pref_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    return time.perf_counter() - start
