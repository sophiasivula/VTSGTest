# Python program to demonstrate
# command line arguments


import getopt, sys
import math
import os

def test():

    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]

    # Options
    options = "hmo:"

    # Long options
    long_options = ["Help", "My_file", "Output="]

    tainted_0 = sys.argv[1]
    tainted_1 = tainted_0

    # No filtering (sanitization)
    tainted_1 = tainted_0


    #flaw
    os.system('ls ' + tainted_1)

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Help"):
                print ("Displaying Help")
                
            elif currentArgument in ("-m", "--My_file"):
                print ("Displaying file_name:", sys.argv[0])
                
            elif currentArgument in ("-o", "--Output"):
                print (("Enabling special output mode (% s)") % (currentValue))
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))






if __name__ == '__main__':
        test()
