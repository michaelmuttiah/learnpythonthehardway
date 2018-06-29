cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
# these are the variables within this equation/code

cars_not_driven = cars - drivers
# as you can only have 1 car per driver!
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
# each car has 4 spaces
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
# every variable in grey must be preceded and followed by a comma
# or it will not run and will have a syntax error
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
