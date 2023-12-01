'''import sys
import subprocess

def main():
    # Check if a command-line argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    # Get the user input
    directory = sys.argv[1]

    # Validate or sanitize the input if necessary
    # For simplicity, let's assume it should be a valid directory name

    # Use subprocess with a list of arguments to avoid command injection
    try:
        subprocess.run(['ls', directory], check=True)
    except subprocess.CalledProcessError:
        print(f"Error: Failed to list directory {directory}")
        sys.exit(1)

if __name__ == '__main__':
    main()

'''

import sys
import subprocess
import shlex

def main():
    # Check if a command-line argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    # Get the user input
    directory = sys.argv[1]

    # Validate or sanitize the input if necessary
    # For simplicity, let's assume it should be a valid directory name

    # Use subprocess with a list of arguments to avoid command injection
    try:
        subprocess.run(['usr/bin/ls', '-u', 'critical', shlex.quote(directory)], check=True)
        #subprocess.run(['/usr/bin/calculator', '-u', 'critical', msg], check=True) # Path qualified from root

    except subprocess.CalledProcessError:
        print(f"Error: Failed to list directory {directory}")
        sys.exit(1)

if __name__ == '__main__':
    main()


