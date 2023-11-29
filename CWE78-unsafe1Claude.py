import os
import sys

def main():
  user_input = sys.argv[1]
  user_input = user_input.strip()

  # Validate input
  if '..' in user_input or '/' in user_input:
    print 'Invalid input'
    return

  os.system('ls '+ user_input)

if __name__ == '__main__':
  main()