# Socket is the endpoint that receives data that is receives that commmunication
import socket

# Where AF_INET Corresponds to the IPV4 and SOCK_STREAM Corresponds to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


full_msg = ''
# recv(1024) is the buffer where data will be received 
while True:

	msg = s.recv(1024)

	if len(msg) <= 0:
		break
		full_msg += msg.decode("utf-8")
print(full_msg)


