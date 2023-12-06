import math
import sys


def main():

    try:
        tainted_2 = int(sys.argv[1])
    except ValueError:
        tainted_2 = 1776

    tainted_3 = tainted_2

    if 1==0:

        if tainted_2 < 0:
            sys.exit("Negative input not allowed")
        tainted_3 = tainted_2

    else:
        pass

    array = [0, 1, 2, 3, 4]

    #flaw # check that tainted_3 < len(array), but not that it is >= 0, so may attempt to read out of array bounds
    if tainted_3 < len(array):
        print(array[tainted_3])
    else:
        print('Array index out of bounds')

    print('Done')


if __name__ == '__main__':
        main()