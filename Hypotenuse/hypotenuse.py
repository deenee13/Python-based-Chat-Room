# python3 hypotenuse.py -L -4 -B -3 ( where values can be different)

import sys
import getopt
from math import sqrt


def hypotenuse_calc():
    # Taking all arguments
    argumentlist = sys.argv[1:]
    print("Total arguments passed:", argumentlist)

    # It takes three arguments
    # 1) Total no. of argument, 2) Shortopt, 3) Longopt
    # Colon means value is expected same for "="
    try:
        opts, args = getopt.getopt(argumentlist, "L:B:", ["Length=", "Breadth="])
        # print(opts, args)

        if len(opts) != 2:
            print(" Wrong number of arguments")

        for opt, arg in opts:
            if opt in ['-L']:
                sqr_length = (int(arg) * int(arg))
            elif opt in ['-B']:
                sqr_breadth = (int(arg) * int(arg))

        # print("Value of Hypotenuse:", sqrt(sqr_length + sqr_breadth))
        
    except getopt.GetoptError as err:
        print(err)

    return(sqrt(sqr_length + sqr_breadth))


# Program1
answer = hypotenuse_calc()
print("Value of Hypotenuse:", answer)
