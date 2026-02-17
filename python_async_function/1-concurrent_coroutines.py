#!/usr/bin/env python3
"""Module that provides an asynchronous wait_n coroutine."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns sorted delays."""
    tasks = [asyncio.create_task(wait_random(max_delay))
             for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
