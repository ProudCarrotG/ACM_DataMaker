import logging
import os
import sys

import coloredlogs


def logging_init(name: str):
    logger = logging.getLogger(name)
    if os.getenv('TEST'):
        coloredlogs.install(level=logging.DEBUG, stream=sys.stdout)
    else:
        coloredlogs.install(level=logging.INFO, stream=sys.stdout)
    return logger
