#!/usr/bin/env python3
"""
    Definess a function that creates and returns a asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns a asyncio.Task with a delay time not more than max_delay. """
    return asyncio.create_task(wait_random(max_delay))
