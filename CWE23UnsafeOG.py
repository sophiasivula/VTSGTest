import math
import os
import sys


def main():

    # no input
    tainted_2 = None

    tainted_3 = tainted_2

    if (math.sqrt(42)<=42):

        tainted_3 = os.environ['ADD']


    if sys.platform == 'linux':
        root = '/home'
    else:
        # MacOS
        root = '/Users'

    if tainted_3 is not None:
        #flaw # no validation - concatenated value could have path traversal
        file = os.path.join(root, tainted_3)
        with open(file, 'r') as f:
            print(f.readline(), end='')

    print('Done')


if __name__ == '__main__':
        main()