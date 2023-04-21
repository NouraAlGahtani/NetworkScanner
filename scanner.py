import socket
import subprocess
import sys
from datetime import datetime


#--------------------------------Clear Screen-----------------------------------------------
subprocess.call('clear', shell=True)


#-------------------------------------Ask for Input-------------------------------------

remoteServer = input("Enter a Remote host to scan :D :")
remoteServerIP = socket.gethostbyname(remoteServer)

#---------------------- Print Banner with information which host we are  about scan-----------------------------------------

print("-" * 60)
print("Please wait , scanning Remote host", remoteServerIP)
print("-"*60)

#----------------------------------check what time the scan started-----------------------------------------------------------

t1 = datetime.now()


#------------------------------------range to scan between ports-------------------------------------------------------------
target_host = "localhost"
port_range = range(1, 1025)

for port in port_range:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    try:
        client.connect((target_host, port))
        print(f"Port {port} is open")
        client.close()
        
    except:
        pass
    
        





