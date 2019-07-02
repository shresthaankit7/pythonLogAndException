#!/usr/bin/python3

import sys
import os
import logging.config

script_root_path = os.path.abspath(os.path.abspath(os.path.dirname(__file__))) + '/'
sys.path.append(script_root_path + 'utils/')

from subClass import SubClass
from utils.dateUtils import DateUtils

logging.config.fileConfig(script_root_path + '/logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

# -------------- Main Class Defination --------------
class Main:
    def __init__(self):
        self._varA = "A"
        self._varB = "B"

    def getVar(self,key):
        if hasattr(self,key):
            return getattr(self,key)
        else:
            raise Exception("Key: " + key + " is not present.")

# -----------------------------------------------------
logger.info("HI")
try:
    main1 = Main()
    print("Getting Var A >>> " + str(main1.getVar("_varA")))

    subClass1 = SubClass()
    print("SubClass get variable >> " + subClass1.getSubVar())

    dateUtils = DateUtils()
    print("Date Utils >> " + dateUtils._testVar)


    print("Testing var C>>> " + str(main1.getVar("_varC")))


except Exception as e:
    print ("Got Exception :\n" + str(e))
    logger.error("Got Exception in Main")


    