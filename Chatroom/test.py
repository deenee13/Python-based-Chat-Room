'''
                        # Extracting the username and the header length of the username of the client where we want to send the message 
                        receiver = clients[client_socket]
                        receiver_username_message = receiver['data'].decode('utf-8')
                        receiver_username_header = (int)(receiver['header'].decode('utf-8'))
                        print(f'value of receiver_username_message is {receiver_username_message}')
                        print(f'value of receiver_username_header is {receiver_username_header}')

                        # Then receiving the message according to the client username's header length(message sending client)
                        message_username = message['data'].decode('utf-8')
                        print(f"type of variable of message_username is {type(message_username)}")
                        print(f"value of message_username is {message_username[0:receiver_username_header]}")

                        if(message_username[0:receiver_username_header] == receiver_username_message):
'''


def get_username(message):
    i = 0 
    for element in message:
        i = i + 1
        if(element == ':'):
            break
    print(f"message is {message[0:i]}")
    return(message[0:i])

def get_dict():
    dict = {}
    fruit = 'orange'
    dict[fruit] = 'fruit'
    fruit1 = dict.get(fruit)
    print(f"{fruit1}")
    print(dict)
    #for value in dict.values():
    #    print(value[0])



if __name__ == '__main__':
    #   message = '@dee:hi'
    #   get_username(message)
    get_dict()