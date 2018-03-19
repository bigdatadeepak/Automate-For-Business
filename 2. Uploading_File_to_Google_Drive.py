#!/usr/bin/env python
"""
Program Name: Banner, Logging and PyDrive
Purpose     : Test best

        #####################     Change log   ###############################
        ##------------------------------------------------------------------##
        ##  Author              ##Date                ##Current Version     ##
        ##------------------------------------------------------------------##
        ## Deepak Kumar         ##11th April,2017     ##V1.0                ##
        ##------------------------------------------------------------------##
        ######################################################################
        Date                Version     Author      Description
        11th April,2017     v 0.1       Deepak      Added Doc String, Logging
"""
print "Program Execution Started...\nImporting the necessary libraries" #Delete this line before sending code to production

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import logging


def Upload_to_Google_Drive(filename_to_upload, name_to_give_uploaded_file= None, file_id= None):
    """
        Purpose: This function will load the file from Local machine to Google Drive

        Args:
            filename_to_upload: Local File that needs to be upload to Google Drive
            name_to_give_uploaded_file: Name that needs to be given to uploaded file in Drive
            file_id: Unique Id for file_to_be_uploaded

        Returns: None
    """   

    if (name_to_give_uploaded_file != None) and (file_id != None):
        print("Can only have Name to Give Uploaded File or File ID to reference an upload")
        exit()

    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

    # Create GoogleDrive instance with authenticated GoogleAuth instance.
    drive = GoogleDrive(gauth)

    # Create GoogleDriveFile instance with title 'Hello.txt'.
    #file1 = drive.CreateFile({'title': 'Hello.txt'})
    file = drive.CreateFile()
    if name_to_give_uploaded_file != None: file['title'] = name_to_give_uploaded_file
    if file_id != None: file['id']=  file_id
    file.SetContentFile(filename_to_upload)
    file.Upload( {"convert" :True }) # Upload the file. Convesrts True puts it into Google Sheets
    logging.info('File Uploaded...title: {0}, id: {1}'.format(file['title'], file['id']))

def log_config():
    """
    Purpose: This function will Configure Log file and print the Doc String

    Args: Nothing

    Returns: None
    You can refer following examples for logging the context.
     logging.debug('This message will get printed in log file')
     logging.info('This message will get printed in log file')
     logging.warning('This message will get printed in log file')
     Logging.error('This message will get printed in log file')
     Logging.critical('This message will get printed in log file')

    """

    global Info_file
    #Logging the Doc String
    with open(Info_file,mode= 'a') as ftr:
        ftr.write(__doc__+"\n\n")
    #Log Configuration
    logging.basicConfig(filename=Info_file,level=logging.DEBUG,
                        format='%(asctime)s- %(name)-12s - %(levelname)-8s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def banner(action,file):
    """
    Purpose: This function will print the "Text" in a banner format

    Args:
        :param action: "Type of Action" you are going to perform
        :param file: "File" on which action is going to be performed

    Returns: None
    """
    global Info_file
    output = "|\
            Action: {action_type} \
            File Under Process: {file_name} \
            |".format(action_type = action, file_name = file)
    banner = '+'+ '-'*(len(output)-2)+'+'
    boarder = '#'+ ' '*(len(output)-2)+'#' #For 1st and last line space
    style = [banner, boarder, output, boarder, banner]
    design = "\n".join(style)
    with open(Info_file,mode= 'a') as ftr:
        ftr.write(design+"\n\n")

if __name__ == "__main__":
    print "Executing the code and generating the Log file"
    log_config()
    logging.info('Starting the program execution\n')
    banner(action = "Reading Input File(s)",file = "Microsite Static Data.xlsx And State Street Sheets")

    Upload_to_Google_Drive(save_path+"\PacificAM Pricing Braude Microsite "+today+".xlsx",  None, Braude_key)
    logging.info("Upload to Google Drive PacificAM Pricing Braude Microsite End\n")
    logging.info("Script Got Completed\n")



