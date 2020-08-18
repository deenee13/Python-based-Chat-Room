
import socket
import sys
import select
import _thread


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

# List to maintain the number of clients joining the server which will contain its address and connection
list_of_clients = {} 

# list to maintain the username along with the address
list_of_username = {}

# Handling connection from multiple clients and saving them in dictionary


def accepting_connections():

    print("In accepting_connection function")
    while True:
        try:
            sockets_list = [sys.stdin, server]  # List of all the clients joining the server
            read_sockets, write_socket, error_socket = select.select(
            sockets_list, [], [])
            for notified_socket in read_sockets:
                if notified_socket == server:
                    conn, address = server.accept()
                    # It prevents timeout from happening
                    server.setblocking(1)
                    print(f"Address  value {conn} ")
                    # Store connections and address in to dictionary
                    list_of_clients.update({address: conn})
                    ## print(list_of_clients)
                    
                    # Update the Sockets list
                    sockets_list.append(conn)  ### This may be of no use ###

                    message = receive_message(conn)

                    message = str(message)

                    # Store the username and the address in to dictionary
                    list_of_username.update({message: address})

                    print(f"Accepted new connection from {address[0]}:{address[1]} with username:{message} ")

                    # creates and individual thread for every user
                    # that connects
                    _thread.start_new_thread( sending_command, (conn, address)) 
        except BaseException:
            print("Error accepting Connections")
            return False

    conn.close()
    server.close()


# This function is to receive messages  (Perfectly correct)
def receive_message(conn):
    print(f"In receive message function")
    try:
        message = conn.recv(2048)

        if not len(message):
            return False

        return(message)

    except:
        return False


def sending_command(conn, address):
    print("In sending_command function")
    #  Sends a message to the client who established connection with the server
    conn.send(str.encode("Welcome to the server"))

    while True:
        try:
            message = receive_message(conn)
            print(f"Message received in Sending Command function is {message}")
            message = str(message)
            for username in list_of_username.keys():
                # print(f"Username out of if statement {username}")
                if username == message:
                    print(username)
                    address_1 = list_of_username[username]
                    # Message received and the address of the client
                    print(f"address of the client {address_1[0]} along with port number {address_1[1]}")
                    print(f"Message from the client is {message}")
                    broadcast(message, address_1[1]) 

                else:
                    print("In else")
                    # link is broken remove the connection
                    remove(conn)
        except BaseException:
            print("In exception")
            continue


def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove[conn]


def broadcast(message, myaddress):
    print("In broadcast message function")
    if not len(list_of_clients):
        print("Client list is empty")
        return False

    print(f'Here is the List of keys {list_of_clients.keys()}')

    for address in list_of_clients.keys():
        print(address[1])
        if address[1] == myaddress:
            conn = list_of_clients[address]
            try:
                ##  print(
                ##    f'print message to send in broadcast function {message}\n')
                ##  print(f'Sending message to {conn}')

                # convert the message which is in bytes into string format
                message = str(message)

                # Send the string format message to client
                conn.send(str.encode(message))
            except BaseException:
                print("Inside the exception condition ")
                print(f"Inside the exception message{conn}")
                conn.close()
        else:
            print(f"Cannot send message to self {address} {myaddress}")


if __name__ == '__main__':
    accepting_connections()
