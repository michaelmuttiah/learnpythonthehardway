from sys import argv

#imports argv module from sys, allowing for arguments

script, filename = argv

# argument variables are set

txt = open(filename)

# opens file contents (i.e. .txt etc.)

print "Here's your file %r:" % filename
print txt.read()

# Lines 10 to 15 have been removed from code in ex15.py
