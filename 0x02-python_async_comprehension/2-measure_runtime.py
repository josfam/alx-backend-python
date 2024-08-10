#!/usr/bin/env python3

"""Coroutine that will execute async_comprehension four times in parallel
using asyncio.gather
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel using asyncio.gather

    Args:
        None
    Returns:
        The total time to run the coroutine
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension(),)
    return time.perf_counter() - start_time
