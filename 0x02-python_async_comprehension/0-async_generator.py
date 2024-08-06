#!/usr/bin/env python3

"""Asynchronous generator the generates a random number between 1 and 10"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times, each time asynchronously waiting 1 second,
    then yields a random number between 0 and 10

    Args:
        None
    Yields:
        A random number between 0 and 10
    """
    LOOP_COUNT = 10
    SLEEP_TIME = 1
    for i in range(LOOP_COUNT):
        await asyncio.sleep(SLEEP_TIME)
        yield random.uniform(0, 10)
