import sys

# This function is where you will work your magic!
#
# Input: the 'names' argument should be a string containing a space-separated
# list of names eg. "matthews booth andrews"
#
# Output: should return a space separated string of names ordered by first vowel
#
def vowellate(names=None):

    # This is where you should write your code!
    return "Hello world"


# You can ignore the code below here.
# It just does the following:
#  1. Check for a list of names passed in via the command line
#  2. Runs the vowellate method above
#  3. Prints the result

# Run the vowellate method and print the result
def run(names=None):
    print(vowellate(names))

# If there is a command line argument then pass it in
if __name__ == '__main__':
    run(sys.argv[1]) if len(sys.argv) == 2 else run()
