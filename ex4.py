# Variable set to an integer
cars = 100
# Variable set to a floating point number
space_in_a_car = 4.0
# Variable set to an integer
drivers = 30
# Variable set to an integer
passengers = 90
# Variable set to the evaluation of some math
cars_not_driven = cars - drivers
# Variable set to the value of drivers
cars_driven = drivers
# Variable set to the evaluation of some math (floating point value in this case)
carpool_capacity = cars_driven * space_in_a_car
# Variable set to the evaluation of some math
# It wouldn't make sense to use floats because partial passengers
# would be weird and scary. Unless you're considering Thing from
# the Addams family. But that's assuming that Thing is a fraction
# of a whole passenger, instead of just 1 passenger.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study drills
# The reason for that error was because he mistyped 'carpool_capacity' as 'car_pool_capacity' on line 8
# A floating point doesn't appear to be necessary for space_in_a_car
