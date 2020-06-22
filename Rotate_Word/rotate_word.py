

def rotate_word(string, rotation):
    length = len(string)
    new_string = ' '
    for i in range(0,length):
        value = ord(string[i])
        value = value + rotation
        value = chr(value)
        new_string += value
    print(new_string)
    


string = 'cheer'
rotation = 7
rotate_word(string, rotation)




