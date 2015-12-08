# Prints a string
print "Mary had a little lamb."
# Prints a string and the result of a formatter, which is also a string
print "Its fleece was white as %s." % 'snow'
# Prints as string
print "And everywhere that Mary went."
# Prints a dot 10 times
print "." * 10 # what'd that do?

# Variable assigned to string
end1 = "C"
# Variable assigned to string
end2 = "h"
# Variable assigned to string
end3 = "e"
# Variable assigned to string
end4 = "e"
# Variable assigned to string
end5 = "s"
# Variable assigned to string
end6 = "e"
# Variable assigned to string
end7 = "B"
# Variable assigned to string
end8 = "u"
# Variable assigned to string
end9 = "r"
# Variable assigned to string
end10 = "g"
# Variable assigned to string
end11 = "e"
# Variable assigned to string
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# This concatinates six strings followed by a space (due to the comma)
# That comma bit is a little weird.
print end1 + end2 + end3 + end4 + end5 + end6,
# This concatinates six strings
print end7 + end8 + end9 + end10 + end11 + end12

# So the comma at the end of line 20 prints both statements out
# on the same line, separated by a space. When it's removed
# the result of 20 and 21 are printed on separate lines
