#!/usr/bin/python3
#Copyright to Mid Set
#Contact me : fb.com/midset00
import time
import os
from socket import socket

host = sys.argv[1]
port = int(sys.argv[2])
s=socket.socket(socket.AF_INET, socket.SOCK_stream)
data=s.recv(1024)
try:
 s.connect((host,port))
except socket.error :
 print ('port is close')
 sys.exit()
time.sleep(2)
print ("trying")
time.sleep(1)
print ('host is alive')
print ('port is open')
