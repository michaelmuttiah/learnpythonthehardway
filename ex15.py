from sys import argv

#imports argv module from sys, allowing for arguments

script, filename = argv

# argument variables are set

txt = open(filename)

# opens file contents (i.e. .txt etc.)

print "Here's your file %r:" % filename

print txt.read()

# Using pydoc file, using extra functions to parse
# certain line
#print txt.readline(1)
#print txt.readline(5)
#print txt.readline(8)

# parses file you have set to open and reads it, printing contents

txt.close()

# close file to save processor and for best practise

print "Type the filename again:"
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()

txt.close()

# prints again as above
