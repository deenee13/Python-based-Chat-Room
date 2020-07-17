import socket
import select
import sys


# Where AF_INET Corresponds to the IPV4 and SOCK_STREAM Corresponds to TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print(" Sufficient arguments have not been provided")
    exit()

# takes the first argument from command prompt as IP address
iP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
port = int(sys.argv[2])

# Username of the client
my_username = input("Username: ")

# Connect to the server
client.connect((iP_address, port))

# Receive Functionality will not be blocking
client.setblocking(False)

# Send the username to the server
client.send(str.encode(my_username))

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, client]
    read_sockets, write_socket, error_socket = select.select(
        sockets_list, [], [])

    for socks in read_sockets:
        if socks == client:
            message = socks.recv(2048)
            print(((message)))
        else:
            message = input(f"{my_username} >")
            client.send(str.encode(message))
            sys.stdout.write(message)
            sys.stdout.flush()
client.close()
