from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C (^C)."
print "If you want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
# w = Writing onto the file (filename) which you have opened
# Or in others words making the file writeable

print "Truncating the file. Goodbye!"
target.truncate()
# truncating empties the file, so its blank

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line 1, line 2, line 3)
# \n = new line

print "And finally, we close it."
target.close()
# best practise we close the file
