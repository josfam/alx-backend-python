#!/usr/bin/env python3

"""Takes in an integer, and waits for a random delay between
    0 and max_delay seconds and eventually returns how long the wait was"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes in an integer, and waits for a random delay between
    0 and max_delay seconds and eventually returns how long the wait was
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
