#!/usr/bin/env python3

"""Asynchronous generator"""

import asyncio
import random
from typing import Generator


async def async_generator():
    """Loops 10 times, each time asynchronously waiting 1 second,
    then yields a random number between 0 and 10
    """
    LOOP_COUNT = 10
    SLEEP_TIME = 1
    for i in range(LOOP_COUNT):
        await asyncio.sleep(SLEEP_TIME)
        yield random.uniform(0, 10)
