# Command to format python file according to the pycodestyle
# autopep8 --in-place --aggressive --aggressive <filename>

import socket
import sys
import select

# Where AF_INET Corresponds to the IPV4 and SOCK_STREAM Corresponds to TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print(" Sufficient arguments have not been provided")
    exit()

# takes the first argument from command prompt as IP address
iP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
port = int(sys.argv[2])

# binds the server to an entered IP address and at the specified port number.
server.bind((iP_address, port))

# listens for 5 active connections. Can be changed afterwards according to
# the convenience
server.listen(5)

# List to maint the list of clients which is nothing but the list of clients
sockets_list = [server]

# Client Dictionary where the clients socket must be the key and the
# username and header will be the value
clients = {}

# user Dictionary where the username must be the key and the client_socket
# will be the value
username_dict = {}

i = 0

# Function to receive the message and message length


def receive_message(client_socket):
    try:

        # receiving the header of the message
        message_header = client_socket.recv(2048)
        ####    print(f"value of the message_header {message_header}")

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return{"header": message_header, "data": client_socket.recv(message_length)}

    except BaseException:
        return False


# function to get the username
def get_username(message):
    # Runnig for loop until ':' is found
    for element in message:
        global i
        i += 1
        if(element == ':'):
            break
    print(f"message is {message[0:i]}")
    # Returning the username
    return(message[0:i])


# Function to differentiate between the Username and the message
def new_message(message):
    # Decodig the received message
    message_new = message['data'].decode('utf-8')
    # Extracing the message from username
    message_new = message_new[i:]
    message_new = message_new.encode('utf-8')
    # Calculating the length of the message
    message_header = f"{len(message_new):<{2048}}".encode("utf-8")
    ####    print(f"value of the message_header {message_header}")

    # Returning the actual length of the message and the header
    return{"header": message_header, "data": message_new}


# main function
def accepting_connections():
    while True:
        global i
        read_sockets, _, exception_socket = select.select(
            sockets_list, [], sockets_list)
        for notified_socket in read_sockets:

            # If received socket is new add the username
            if notified_socket == server:
                client_socket, client_address = server.accept()

                user = receive_message(client_socket)
                if user is False:
                    continue

                # Add new connection to list
                sockets_list.append(client_socket)

                clients[client_socket] = user
                # print(f"clients: {clients}")

                # To extract the client socket after wards
                username = user['data'].decode('utf-8')
                username_dict[username] = client_socket
                # print(f"username_dict: {username_dict}")

                print(
                    f"Accepted new connection from {client_address[0]}:{client_address[1]} with username:{user['data'].decode('utf-8')}")

            else:
                # receive the message from the client
                message = receive_message(notified_socket)

                # Draw the username of the client sending the message
                user = clients[notified_socket]

                print(
                    f"received message from {user['data'].decode('utf-8')}    : {message['data'].decode('utf-8')}")

                # If there is no message then remove the connection
                if message is False:
                    print(
                        f"Closed Connection from {clients[notified_socket]['data'].decode('utf-8')}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue

                # To check wether there is username in the message
                message_data = message['data'].decode('utf-8')

                # If there is '@' at the start of the message then there is
                # username
                if(message_data[0] == '@'):
                    username = get_username(message_data)
                    print(f'username is {username}')

                    # Extract the socket to send the message to with the unique
                    # username
                    client_socket = username_dict.get(username)
                    print(f'client_socket is {client_socket}')

                    # if the username entered by the user is not valid display wrong username message in server
                    # You can also sent that particular message to the client
                    if client_socket is None:
                        print(f"user entered wrong username")

                        # reset global i to receive next message properly
                        i = 0
                    # If it is valid extract the message and send it to the
                    # specific client
                    else:
                        message = new_message(message)
                        client_socket.send(
                            user['header'] +
                            user['data'] +
                            message['header'] +
                            message['data'])
                        i = 0

                # if there is no '@' in the message, broadcast the message to
                # except itself
                else:
                    # For loop to prevent sending message to itself
                    for client_socket in clients:
                        if client_socket != notified_socket:
                            client_socket.send(
                                user['header'] +
                                user['data'] +
                                message['header'] +
                                message['data'])

        for notified_socket in exception_socket:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]


# Start point of the program
if __name__ == '__main__':
    accepting_connections()
