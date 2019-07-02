#!/usr/bin/python3

import logging.config

logging.config.fileConfig('/home/ankshrestha/MYWORKSPACE/myGit/pythonLogAndException/logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class SubClass:

    def __init__(self):
        logger.info("Initaialize Subclass")
        self.subVar = "XYZ"

    def getSubVar(self):
        return getattr(self,"subVar")

