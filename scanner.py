import socket
import subprocess
import sys
from datetime import datetime


#--------------------------------Clear Screen----------------------------------
subprocess.call('clear', shell=True)


#-------------------------------------Ask for Input-----------------------------

remoteServer = input("Enter a Remote host to scan :D :")
remoteServerIP = socket.gethostbyname(remoteServer)



