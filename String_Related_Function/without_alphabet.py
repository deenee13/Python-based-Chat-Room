import helper




def check_alphabet(mystr, alphabet):
    result = alphabet in mystr.lower()
    print(result)
    return(result)


def main():
    argument_dict = {"string": ["Enter string to check", "str"], "alphabet": ["Enter alphabet to check", "str"]}
    args = helper.helper_parse_argument(argument_dict)

    result = check_alphabet(args.string, args.alphabet)
    if result is True:
        print("String: " + args.string + " have letter: " + args.alphabet + " in it")
    elif result is False:
        print("String: " + args.string + " don't have letter: " + args.alphabet + " in it")



if __name__ == '__main__':
    main()

