import logging

import yarqueue
import redis

LOGGER = logging.getLogger(__name__)


def consume():

    queue = yarqueue.Queue(
        name="example",
        redis=redis.Redis()
    )

    LOGGER.info("waiting...")

    while True:
        data = queue.get()
        LOGGER.info(data)
