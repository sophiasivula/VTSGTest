import os
import math
import sys

# Function to count number
# of characters, words, spaces
# and lines in a file
def counter(fname):
	
    # variable to store total word count
    num_words = 0
	
    # variable to store total line count
    num_lines = 0
	
    # variable to store total character count   
    num_charc = 0
	
    # variable to store total space count
    num_spaces = 0
	

    arg1 = sys.argv[1]
    arg2 = arg1

    # No filtering (sanitization)
    arg2 = arg1


    print(f'file "{ arg2 }" ', end='')
    #flaw
    if os.path.exists(arg2):
        print('exists')
    else:
        print('does not exist')


	# opening file using with() method
	# so that file gets closed
	# after completion of work
    with open(fname, 'r') as f:
		
		# loop to iterate file
		# line by line
	    for line in f:
			
			# separating a line from \n character
			# and storing again in line
		    line = line.strip(os.linesep)
			
			# splitting the line
            wordslist = line.split()
			
			# incrementing value of num_lines
            num_lines = num_lines + 1
			
			# incrementing value of num_word
            num_words = num_words + len(wordslist)
			
			# incrementing value of num_char
		    num_charc = num_charc + sum(1 for c in line if c not in (os.linesep, ' '))
			
			# incrementing value of num_space
		    num_spaces = num_spaces + sum(1 for s in line if s in (os.linesep, ' '))
    
    
	
	# printing total word count
    print("Number of words in text file: ",
		num_words)
	
	# printing total line count
    print("Number of lines in text file: ",
		num_lines)
	
	# printing total character count
    print("Number of characters in text file: ",
		num_charc)
	
	# printing total space count
    print("Number of spaces in text file: ",
		num_spaces)

# Driver Code:
if __name__ == '__main__':
	fname = 'File1.txt'
	try:
		counter(fname)
	except:
		print('File not found')





############################### CWE Unsafe Args

'''import math
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
'''
