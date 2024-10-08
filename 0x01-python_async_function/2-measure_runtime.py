#!/usr/bin/env python3
"""
    Defines a function that measure the execution time of an async routine.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Returns time of execution in seconds. """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))

    return time.perf_counter() - start
