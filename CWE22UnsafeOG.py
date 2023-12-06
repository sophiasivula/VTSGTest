import math
import os
import sys


def main():
    tainted_0 = sys.argv[1]
    tainted_1 = tainted_0

    # No filtering (sanitization)
    tainted_1 = tainted_0


    print(f'file "{ tainted_1 }" ', end='')
    #flaw
    if os.path.exists(tainted_1):
        print('exists')
    else:
        print('does not exist')


if __name__ == '__main__':
        main()
