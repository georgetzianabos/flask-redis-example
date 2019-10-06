""""Consume message from queue

Usage:
  example consume
"""
import logging

from docopt import docopt

from .consumer import consume

LOGGER = logging.getLogger(__name__)


def cli():

    arguments = docopt(__doc__)

    logging.basicConfig(level=logging.INFO)

    if arguments['consume']:
        consume()
