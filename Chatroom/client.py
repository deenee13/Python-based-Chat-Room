# Socket is the endpoint that receives data that is receives that commmunication
import socket
import time

# Where AF_INET Corresponds to the IPV4 and SOCK_STREAM Corresponds to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
	msg = s.recv(1024)
	if len(msg) <= 0:
		print("Error Case")
		break

	print(msg)


