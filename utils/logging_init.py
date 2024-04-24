import logging
import os
import sys

import coloredlogs


def logging_init(name: str):
    logger = logging.getLogger(name)
    if os.getenv('TEST') == 1:
        coloredlogs.install(level='DEBUG', stream=sys.stdout)
    else:
        coloredlogs.install(level='DEBUG', stream=sys.stdout)
    return logger
