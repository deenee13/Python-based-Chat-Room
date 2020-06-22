# Socket is the endpoint that receives data
import socket
import threading
import time

# This imports specific object from the class queue
from queue import Queue

# Creating a constant for threads
NUMBER_OF_THREADS = 2
# Thread number
JOB_NUMBER = [1, 2]

# It returns the upperbound limit of queue
queue = Queue()

# Create and empty dictionary
connection_address = {}

# Where AF_INET Corresponds to the IPV4 and SOCK_STREAM Corresponds to TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

# listen queue of 5
s.listen(5)

# Handling connection from multiple clients and saving them in dictionary
def accepting_connections():

    print("In accepting_connection function")
    while True:
        try:
            serversocket, address = s.accept()
            s.setblocking(1)  # It prevents timeout from happening

            # Store connections and address in to dictionary
            connection_address.update({serversocket: address})
            # print(connection_address)
            print("Connection has been established in socket", address)

        except:
            print("Error accepting Connections")

# Sending Command to all connected client
def sending_command():
    print(" In Sending Command function")
    while True:
        try:
            # Delay of 1 minute
            time.sleep(10)
            # looping through the Dictionary
            for x in connection_address:

                # Store the keyvalue in temporary variable
                temp_serversocket = x
                print(temp_serversocket)
                t = time.localtime()   # Fetching the local time

                # convert the local time in to the specified format
                current_time = time.strftime("%H:%M:%S", t)
                print("current time: %s", current_time)
                temp_serversocket.send(str.encode(current_time))  # Send to the particular client

        except:
            print("Error Sending Command")
            del connection_address[x]
            pass

# Creating Threads
def create_thread():
    print(" In Create Thread function")
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True   # It ends the thread as program ends to save memory
        t.start()


def create_jobs():
    print(" In create_job Function")
    for x in JOB_NUMBER:
        queue.put(x)        # puts the elements inside the queue

    queue.join()

# Get the thread from queue and do the job
def work():
    print(" In work Function")
    while True:
        x = queue.get()     # fetches the element from the queue 
        if x == 1:
            accepting_connections()
        if x == 2:
            sending_command()
        queue.task_done()    


create_thread()
create_jobs()
