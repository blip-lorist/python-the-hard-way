# Print method with string argument
print "I will now count my chickens:"
# Print seems to take two arguments, the first a string, the second
# is the evaluation of some math. The original didn't use floats,
# and instead drops the digits after the decimal
# (It does NOT round to the nearest whole number!).
print "Hens", 25 + 40 / 6.0 # remember to use the floating point for division
# This uses PEMDAS. First 25*3 is solved, so it's 100 - 75 % 4. Then the
# modelo is solved, making it 100 - 3, then subtraction is solved to reach
# 97
print "Roosters", 100 - 25 * 3 % 4
# Print method with string argument
print "Now I will count the eggs:"
# Print method with an argument evaluating math.
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4.0 + 6
# Print method with a string argument
print "Is it true that 3 + 2 < 5 - 7?"
# Print method evaluating the result of a <
print 3 + 2 < 5 - 7
# Print method taking two arguments, a string and a math evaluation
print "What is 3 + 2?", 3 + 2
# Print method taking two arguments, a string and a math evaluation
print "What is 5 - 7?", 5 - 7
# Print method with string argument
print "Oh, that's why it's False."
# Print method with string argument
print "How about some more."
# Print method with two arguments, a string and the result of evaluating a greater than statement
print "Is it greater?", 5 > -2
# Print method with two arguments, a string and the result of evaluating a greater than or equal to statement
print "Is it greater or equal?", 5 >= -2
# Print method with two arguments, a string and the result of evaluating a less than or equal to statement
print "Is it less or equal?", 5 <= -2
