import math
import os
import sys


def main():
    tainted_0 = sys.argv[1]
    tainted_1 = tainted_0

    # No filtering (sanitization)
    tainted_1 = tainted_0


    #flaw
    os.system('ls ' + tainted_1)


if __name__ == '__main__':
        main()