#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import sys

#Sending email with attachment using Python
attached_file = "C:\\Users\\Deep\\PycharmProjects\\Data_Engineering\\data\\output\\100-Ajit-Rout.pdf"
recipients = ['gecdeepakkumarbehera@gmail.com', 'bigdatadeepak@gmail.com']
emaillist = [elem.strip().split(',') for elem in recipients]


msg = MIMEMultipart()
msg['Subject'] = str("Invoice_PYTHON_COURSE")
msg['From'] = 'bigdatadeepak@gmail.com'
msg['Reply-to'] = 'bigdatadeepak@gmail.com'

msg.preamble = 'TEST.\n'

part = MIMEText("Hi, please find the attached file")
msg.attach(part)

part = MIMEApplication(open(str(attached_file), "rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
msg.attach(part)


server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("bigdatadeepak@gmail.com", "##YOUR_Password_Please##")

server.sendmail(msg['From'], emaillist, msg.as_string())
