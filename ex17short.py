from sys import argv; from os.path import exists
script, from_file, to_file = argv
print "Copying from %s to %s ." % (from_file, to_file)
in_file = open(from_file); indata = in_file.read()
print "The input file is %d bytes long." %len(indata)
print "Does the output file exist? %r" %exists(to_file)
print "Read, hit RETURN to continue, CTRL-C to abort."
raw_input()
out_file = open(to_file, 'w'); out_file.write(indata)
print "Allright, all done."
out_file.close(); in_file.close()

# This is the shortest I can make it, 1 line ... wtf
# I'm sure there is a library I just don't know
# Though unsure how you can get all that text printed
# I suppose 1 line to just execute the script
