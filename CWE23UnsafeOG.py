import math
import sys


def main():

    # no input
    tainted_2 = None

    tainted_3 = tainted_2

    if 1==1:

        tainted_3 = input() # read one line


    if tainted_3 is not None:
        #flaw # no validation - concatenated value allows arbitrary execution
        sys.path += [tainted_3]
        print(f'added { tainted_3 } to Python module search path')

    print('Finished')


if __name__ == '__main__':
        main()