#!/usr/bin/env python
"""
Program Name: install_my_library
Purpose     : Installation of all necessary libraries that doesn't come by default with Python

        #####################     Change log   ###############################
        ##------------------------------------------------------------------##
        ##  Author              ##Date                ##Current Version     ##
        ##------------------------------------------------------------------##
        ## Deepak               ##11th May,2017       ##V1.0                ##
        ##------------------------------------------------------------------##
        ######################################################################
        Date                Version     Author      Description
        17th July,2017       v 0.1       Deepak      Written install_lib function
"""


import subprocess
import logging
import datetime
import xml.etree.ElementTree as ET
from pathlib2 import Path as validate_path
from os import path

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

def xml_read(config_file):
    """
    This function will read the xml through ElementTree and retuen the required attribute values
    Argument: xml file path
    return: dropboxpath path
    """
    tree = ET.parse(config_file)
    root = tree.getroot()

    independentlibrary_list = root.find("independentlibrary").text.split(",")
    dependentlibrary_list = root.find("dependentlibrary").text.split(",")

    return independentlibrary_list,dependentlibrary_list

def banner(logfile,lib_type,lib):
    """
    Purpose: This function will print the "Text" in a banner format

    Args:
        :param action: "Type of Action" you are going to perform
        :param file: "File" on which action is going to be performed

    Returns: None
    """
    output = "|\
            Library Type: {type} \
            Library Under Process: {lib_name} \
            |".format(type = lib_type, lib_name = lib)
    banner = '+'+ '-'*(len(output)-2)+'+'
    boarder = '#'+ ' '*(len(output)-2)+'#' #For 1st and last line space
    style = [banner, boarder, output, boarder, banner]
    design = "\n".join(style)
    with open(logfile,mode= 'a') as ftr:
        ftr.write(design+"\n\n")

def install_lib(lib):
    msg =  "Installation Started For: " + lib
    logging.info(msg+'\n')
    cmd = "pip install " + lib
    try:
        output = subprocess.check_output(cmd)
        logging.info(output+'\n')
    except subprocess.CalledProcessError:
        msg = "Could not find a matching distribution version for {0}".format(cmd.split()[-1])
        logging.info(msg+'\n')
        return 1

if __name__ == "__main__":
    print "Please wait while we install the libraries and generate the Log file for you..."
    config_file = path.join(path.dirname(path.realpath(__file__)), "config_install_my_library.xml")
    independentlibrary_list, dependentlibrary_list = xml_read(config_file)
    project_path =  path.dirname(path.dirname(path.dirname(path.realpath(__file__))))

    logpath = path.join(project_path, "logs\\Log_install_my_library")
    logfile = log_config(logpath,change_log=__doc__)

    try:
        """
        bloomberg_path1 = validate_path("C:\\blp\\API")
        bloomberg_path1.resolve()
        bloomberg_path2 = validate_path("C:\\blp\\DAPI")
        bloomberg_path2.resolve()
        """
        for lib in independentlibrary_list:
            lib_type = "Independent"
            banner(logfile,lib_type,lib)
            install_lib(lib)

        for lib in dependentlibrary_list:
            lib_type = "Dependent"
            banner(logfile,lib_type,lib)
            ret = install_lib(lib)
            if lib == dependentlibrary_list[-1]:
                break
            elif ret == 1:
                msg = "Halting the installation of other libraries "+ str(dependentlibrary_list[dependentlibrary_list.index(lib)+1:])+" due to dependancy with FAILED library " + lib
                logging.info(msg+'\n')
                break
    except WindowsError:
        msg =  "Bloomberg is not installed(properly) at its default path."
        logging.info(msg+'\n')
    finally:
        msg = "Program Execution Completed"
        logging.info(msg+'\n')
        print "Execution completed. You may go through the Log file for detail information."
