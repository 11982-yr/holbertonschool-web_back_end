#!/usr/bin/env python3
"""Module that provides a task_wait_n coroutine."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times and returns sorted delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
