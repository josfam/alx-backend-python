#!/usr/bin/env python3

"""Spawning different co-routines, and sorting their delay times"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes an int and a delay, then spawns a wait_random co-routine n times.

    Args:
        n: The number of times to spawn a wait_random co-routine
        max_delay: The maximum time for a pause of the co-routine

    Returns:
        A list, sorted in ascending order, of the time spent delaying
    """
    delays: List[float] = []
    for count in range(n):
        delay = await task_wait_random(max_delay)

        # sort the delays manually
        current_delays = delays[:]
        if not len(current_delays):
            delays.append(delay)
            continue

        for idx, current_delay in enumerate(current_delays):
            if delay <= current_delay:
                delays.insert(idx, delay)
                break
            if idx == len(current_delays) - 1:
                delays.append(delay)
    return delays
