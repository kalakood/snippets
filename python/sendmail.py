# python3 send.py server from@example.com to@example.com subject "content" 
import smtplib
from smtplib import *
import sys
print(sys.argv)
message = """
From:{}
To:{}
Subject:{}
 
{}
""".format(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
print(message)
try:
  server = smtplib.SMTP(sys.argv[1])
  server.sendmail(sys.argv[2],sys.argv[3], message)
  server.quit()
except Exception as e:
  print(e)
