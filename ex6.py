x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't" #Variable defined as cannot contain an apostrophe in strong
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r" % x # 1 string inside a string
print "I also said: '%s'" % y # 2 string inside a string

hilarious = False # Boolean Value set
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # 3 string inside a string

w = "This is the left side of..."
e = "a string with a right side."

print w + e # Just a way to add 2 alphanumeric values as a string

# 4 string inside a string
