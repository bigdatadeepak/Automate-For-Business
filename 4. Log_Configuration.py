#!/usr/bin/env python
"""
Program Name: log_config.py
Purpose     : Commonly Used function for log mechanism

        #####################     Change log   ###############################
        ##------------------------------------------------------------------##
        ##  Author              ##Date                ##Current Version     ##
        ##------------------------------------------------------------------##
        ## Deepak               ##11th May,2017       ##V1.0                ##
        ##------------------------------------------------------------------##
        ######################################################################
        Date                Version     Author      Description
        17th July,2017       v 0.1       Deepak      Written function for log configuration
"""

import logging
import datetime


def log_config(logpath,change_log):
    """
    Purpose: This function will Configure Log file

    Args: Absolute path of 'logfile'

    Returns: Log File Path
    You can refer following examples for logging the context.
     logging.debug('This message will get printed in log file')
     logging.info('This message will get printed in log file')
     logging.warning('This message will get printed in log file')
     Logging.error('This message will get printed in log file')
     Logging.critical('This message will get printed in log file')

    """

    now = datetime.datetime.now()
    today = now.strftime("%d-%m-%Y")
    time_stamp = today + "_" + now.strftime("%H-%M-%S")
    logfile = logpath + "_" + time_stamp + ".log"

    #Logging the Doc String
    with open(logfile,mode= 'a') as ftr:
        ftr.write(change_log+"\n\n")
    #Log Configuration
    logging.basicConfig(filename=logfile,level=logging.DEBUG,
                        format='%(asctime)s- %(name)-12s - %(levelname)-8s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    logging.info('Starting the program execution\n')
    return logfile
