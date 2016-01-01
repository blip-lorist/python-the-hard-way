from sys import argv

script, first, second, third = argv 
#You must pass at least four arguments in, otherwise you will 
# get a 'ValueError: need more than X values to unpack.
fourth = raw_input("Please enter a fourth argument: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth


