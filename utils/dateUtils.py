#!/usr/bin/python3

import sys
import os
import logging.config

script_root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__))) + '/../'


logging.config.fileConfig(script_root_path + '/logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

class DateUtils:
    def __init__(self):
        self._testVar = "My test Var"
        logger.info("Date Utils initalized")
