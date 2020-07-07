#################################################################
# Date: 06/30/2020
# Name: Deepen Parmar
# Description: This code is about the Server broadcasting the
# message to all the Connected clients
##
##################################################################

# Socket is the endpoint between receiving and sending data
import socket
import time

# Where AF_INET Corresponds to the IPV4 and SOCK_STREAM Corresponds to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# While loop to monitor if there has been any new message or not
while True:
    msg = s.recv(1024)
    if len(msg) <= 0:
        print("Error Case")
        break

    print(msg)
