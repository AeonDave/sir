#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/sir)
See the file 'LICENSE' for copying permission
"""

import logging, sys

logger = logging.getLogger('sirLogger')
stream = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("\r[%(levelname)s] %(message)s", "%H:%M:%S")
stream.setFormatter(formatter)
logger.addHandler(stream)
logger.setLevel(logging.INFO)