#!/usr/bin/python3

from subClass import SubClass

import logging.config

logging.config.fileConfig('/home/ankshrestha/MYWORKSPACE/myGit/pythonLogAndException/logging.ini', disable_existing_loggers=False)
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
    print("HH>>> " + str(main1.getVar("_varA")))

    subClass1 = SubClass()
    print("TTT>> " + subClass1.getSubVar())

    print("HH>>> " + str(main1.getVar("_varC")))


except Exception as e:
    print ("Got Exception :\n" + str(e))
    logger.error("GOT Error here!!!!")


    