


import math
import os
import sys


def main():

    # no input
    tainted_0 = None

    tainted_1 = tainted_0

    tainted_1 = input() # read one line


    if sys.platform == 'linux':
        root = '/home'
    else:
        # MacOS
        root = '/Users'

    if tainted_1 is not None:
        #flaw # no validation - concatenated value could have path traversal
        file = os.path.join(root, tainted_1)
        with open(file, 'r') as f:
            print(f.readline(), end='')

    print('Done')


if __name__ == '__main__':
        main()