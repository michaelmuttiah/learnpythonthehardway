people = 40
cars = 20
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
#elif function means else if, so the if function is FALSE so we move to the
#elif function, each time the computer asks if this is TRUE
else:
    print "We can't decide."
#We need this for if the two values are equal

if buses < cars:
    print "There's too many buses."
elif buses > cars:
    print "Maybe we could take the buses"
else:
    print "We still can't decide"

if people < buses:
    print "Alright, lets just take the buses."
else:
    print " Fine let's stay home then"
