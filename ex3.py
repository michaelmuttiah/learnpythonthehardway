
print "I will now count my chickens:"

print "Hens", 25+30/6 #I first thought this sum was wrong, as in calculating 25 + 30
# =55 then dividng by 6, but is in fact 25 +(30/6)

print "Roosters", 100 - 25 * 3 % 4
#Same here so this is 100 - (25*3%4)

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4.0 + float(6)

#To return a float for this value there are three ways, two are as above
#Writing one number as a float i.e. 4.0 , writing float(n)
#Or much easier in future is importing division as a function
#from __future__ import division

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?" , 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5>= -2
print "Is it less or equal?", 5 <= -2
