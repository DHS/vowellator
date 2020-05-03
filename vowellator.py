import csv
import sys

# This specifies the csv name of the file that will contain the names to use.
# It can be changed as desired
EXAMPLE_CSV = "example.csv"

# This function is where you will work your magic!
#
# Input: the 'names' argument should be a string containing a space-separated
# list of names eg. "matthews booth andrews"
#
# Output: should return a space separated string of names ordered
# by first vowel e.g. "andrews matthews booth"
# Exercise: How should names that contain the same first vowel be returned?
#
def vowellate(names=None):    
    # This is where you should write your code!
    return "Hello world"


# You can ignore the code below here.
# It just does the following:
#  1. Find the csv of names
#  2. Return the names in the csv in a format vowellate can interpret
#  2. Runs the vowellate method passing the names as a keyword argument
#  3. Prints the result


# Find the csv of names supplied and return them in a format vowellate can use
# csv should 
def read_csv(filename):
    name_list = ""
    with open(filename, 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            name_list = name_list + row[0] + " "
        name_list = name_list[:-1]
    return name_list


# Find names, run the vowellate method and print the result
def run(filename=None):
    if not filename:
        filename = EXAMPLE_CSV
    filename = "namefiles/" + filename
    names = read_csv(filename)
    print(vowellate(names=names))


# Run the script from command line
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        run(args[1])
    elif len(args) < 2:
        run()
    else:
        raise TypeError("Please provide 1 or 0 arguments")
