#!/usr/bin/env python3

"""Measuring the runtime of an asyncio function"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n: The number of times to spawn a wait_random co-routine
        max_delay: The maximum time for a pause of the co-routine

    Returns:
        The approximate amount of time taken for each run of co-routines
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))  # running the asyncio subroutine
    total_time = time.perf_counter() - start_time
    return total_time / n
