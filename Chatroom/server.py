# Socket is the endpoint that receives data that is receives that commmunication
import socket
print("Deepen")

# Where AF_INET Corresponds to the IPV4 and SOCK_STREAM Corresponds to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))

# listen queue of 5
s.listen(5)

while True:
    clientsocket, address = s.accept()

    print("Connection has been established",address)
    clientsocket.send(bytes("Welcome to the server!" , "utf-8"))
    clientsocket.close()
