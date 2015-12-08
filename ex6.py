# Sets 'x' variable to a string with a format character that
# takes an integer
x = "There are %d types of people." % 10
# Sets 'binary' variable to a string
binary = "binary"
# Sets 'do_not' variable to a string
do_not = "don't"
# Sets 'y' variable to a string containing two string format characters
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the string and integer contained in x
print x
# Prints the strings contained in y
print y
# Prints any format passed in through this formatter (in this case,
# a string and an integer)
print "I said: %r." % x
# Prints strings
print "I also said: '%s'." % y

# Sets 'hilarous' variable to the boolean value of false
hilarious = False
# Sets 'joke_evaluation' variable to a string that will take any
# format at the end
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints a string followed by the boolean value contained
# in hilarious
print joke_evaluation % hilarious

# Sets 'w' variable to a string
w = "This is the left side of ..."
# Sets 'e' variable to a string
e = "a string with a right side."

# Prints the combined string of concatinating w and e
print w + e

# There are four places where strings are in strings
# Twice on 9, then on lines 14 and 19

# Concatination
