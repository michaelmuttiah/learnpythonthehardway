from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

# print all function set as f, opens and reads the file, then prints text

def rewind(f):
    f.seek(0)

# rewind functions, seeks back to 0, as in goes back to the beginning

def print_a_line(line_count, f):
    print line_count, f.readline()

# functions print a line, prints line count from the file and its text

current_file = open(input_file)

# opens the file that you have called

print "First, let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print 3 lines."

current_line = 1
print_a_line(current_line, current_file)

# print a line prints line number, and also from the current file that is open

current_line += 1 # rewritten with += instead of = current_line + 1
print_a_line(current_line, current_file)

# now current_line = 2

current_line += 1
print_a_line(current_line, current_file)

# now current_line = 3
