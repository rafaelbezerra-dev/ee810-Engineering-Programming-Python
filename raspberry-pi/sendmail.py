#!/usr/bin/python

import smtplib
import time
from socket import *

time.sleep(20)
# print "retrieving local ip address"	
s = socket(AF_INET, SOCK_DGRAM)
s.connect(("gmail.com", 80))
local_ip_addr = s.getsockname()[0]
s.close()


username = '@gmail.com'
password = ''
fromaddr = username
toaddrs  = ''
msg = "\r\n".join([
  "From: " + fromaddr,
  "To: " + toaddrs,
  "Subject: Just a message",
  "",
  local_ip_addr
  ])
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()