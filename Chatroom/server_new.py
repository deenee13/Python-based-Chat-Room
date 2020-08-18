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

# Client Dictionary where the clients socket must be the key and the user data will be the value 
clients = {}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(2048)
        if not len(message_header):
            return False
        
        message_length = int(message_header.decode("utf-8").strip()) # Try these without using decode later
        return{"header": message_header, "data": client_socket.recv(message_length)}
    
    except:
        return False




def accepting_connections():
    while True:
        read_sockets, _, exception_socket = select.select(sockets_list, [], sockets_list)
        for notified_socket in read_sockets:
            if notified_socket == server:
                client_socket, client_address = server.accept()

                user = receive_message(client_socket)
                if user is False:
                    continue

                sockets_list.append(client_socket)

                clients[client_socket] = user
                #   print(f"client dictionary is {clients}")

                print(f"Accepted new connection from {client_address[0]}:{client_address[1]} with username:{user['data'].decode('utf-8')}")
            
            else:
                message = receive_message(notified_socket)

                if message is False:
                    print(f"Closed Connection from {clients[notified_socket]['data'].decode('utf-8')}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue
                user = clients[notified_socket]
                print(f"received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
        
        for notified_socket in exception_socket:
            socket_list.remove(notified_socket)
            del clients[notified_socket]


if __name__ == '__main__':
    accepting_connections()




                 





