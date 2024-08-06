#!/usr/bin/env python3

"""Returning a Task object"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay: The maximum time for a pause of the co-routine

    Returns:
        A Task object
    """
    return asyncio.create_task(wait_random(max_delay))
