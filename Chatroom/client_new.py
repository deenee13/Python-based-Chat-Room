import sys
import socket
import select
import errno

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

username = my_username.encode("utf-8")
username_header = f"{len(username):<{2048}}".encode("utf-8")

# Send the username to the server
client.send((username_header + username))

while True:
    message = input(f"{my_username} > ")

    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{2048}}".encode("utf-8")
        client.send(message_header + message)

    try:
        while True:
            # Receive things
            username_header = client.recv(2048)
            if not len(username_header):
                print("connection closed by server")
                sys.exit()

            username_length = int(username_header.decode("utf-8").strip())
            username = client.recv(username_length).decode("utf-8")

            message_header = client.recv(2048)
            message_length = int(message_header.decode("utf-8").strip())
            message = client.recv(message_length).decode("utf-8")
            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
            print('reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('general eror', str(e))
        sys.exit()
