print "How old are you?",
age = raw_input("age prompt --> ") # this is like ruby's 'chomp', it allows you to get user input
print "How tall are you?",
height = raw_input("height prompt --> ")
print "How much do you weigh?", #print statements end with new lines, so the commas keep the input on the same line
weight = raw_input("weight prompt --> ")

print "So you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# Raw_input takes one optional parameter, prompt string. 
# Avoid input() because there are security issues with that. 
