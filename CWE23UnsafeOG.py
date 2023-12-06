import math
import os
import sys


def main():
    tainted_0 = os.environ['ADD']
    tainted_1 = tainted_0

    # No filtering (sanitization)
    tainted_1 = tainted_0


    # convert input string to number
    try:
        number_of_loops = int(tainted_1)
    except ValueError:
        print('Invalid input.  Numeric input expected.  Assuming 1.')
        number_of_loops = 1

    #flaw
    for j in range(number_of_loops):
        print('Hello, world')


if __name__ == '__main__':
        main()