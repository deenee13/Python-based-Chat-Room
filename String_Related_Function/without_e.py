import argparse


def check_e(string):
    length = len(string)
    print("Length of the string:", length)
    for i in range(0,length):
        if(string[i] == 'e'):
            print("String has letter e")
            return (False)
            break
        elif(string[i] == 'E'):
            print("String has letter E")
            return (False)
            break
        else:
            pass
    return(True)

    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help = "enter Word you wish to test", type=str)
    args = parser.parse_args()
    print(args.string)
    result = check_e(args.string)
    if(result == True):
        print("String don't have letter e in it")
    elif(result == False):
        print("String have letter e in it")


if __name__ == '__main__':
    main()