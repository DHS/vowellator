import sys

# This function is where you will work your magic!
#
# Input: the 'names' argument passed to the function should be a string
# containing a space-separated list of names
# eg. "toller edwards aldrich"
#
# Output: the function should return a string containing a
# space-separated list of names ordered by first vowel
# eg. "aldrich edwards toller"
#
def vowellate(names=None):

    # This is where you should write your code!
    return "Hello world"


# You can ignore the code below here.
# It just does the following:
#  1. Check for a list of names passed in via the command line
#  2. Run the vowellate function
#  3. Print the result

# Run the vowellate function and print the result
def run(names=None):
    print(vowellate(names))

# If there is a command line argument then pass it in
if __name__ == '__main__':
    run(sys.argv[1]) if len(sys.argv) == 2 else run()
