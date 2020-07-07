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

# listens for 5 active connections. Can be changed afterwards according to the convenience
server.listen(5)

# List to maintain the number of clients joining the server 
list_of_clients = {}

# Handling connection from multiple clients and saving them in dictionary


def accepting_connections():

    print("In accepting_connection function")
    while True:
        try:
            conn, address = server.accept()
            server.setblocking(1)  # It prevents timeout from happening
            print(f"Connection value {conn} and address {address}")
            # Store connections and address in to dictionary
            list_of_clients.update({address: conn})
            print(list_of_clients)
            print("Connection has been established in socket", {address [0]})
            # creates and individual thread for every user  
            # that connects 
            _thread.start_new_thread(sending_command,(conn,address)) # change the function
        except:
            print("Error accepting Connections")
    
    conn.close ()
    server.close () 



def sending_command(conn, address):
    print("In sending_command function")
    #  Sends a message to the client who established connection with the server
    conn.send(str.encode("Welcome to the server"))

    while True:
        try:
            message = conn.recv(2048)
            if message:

                # Message received and the address of the client
                print("address of the client is", address[0] )
                print("Along with the message", message)
                broadcast(message, address)
            
            else:
                # link is broken remove the connection 
                remove(conn)
        except:
            continue
        
def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove[conn]

def broadcast(message, myaddress):
    print("In broadcast message function")
    if not len(list_of_clients):
        print("Client list is empty")
        return

    print(f'Here is the List of keys {list_of_clients.keys()}')

    for address in list_of_clients.keys():
        print(address)
        if address != myaddress:
            conn = list_of_clients[address]
            try:
                print(f'Sending message to {conn}')
                conn.send("HELLO")
            except:
                print("Inside the exception condition ")
                conn.close()
        else:
            print(f"Cannot send message to self {address} {myaddress}")

if __name__ == '__main__':
    accepting_connections()
