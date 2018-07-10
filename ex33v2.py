# Borrowed from: https://github.com/jdorfman/thehardway/blob/master/ex33.py

i = 0
numbers = []

def theloop(numb,plusnum):
        global i
        while i < numb:
            print "At the top of i is %d" % i
            numbers.append(i)

            i = i + plusnum
            print "Numbers now: ", numbers
            print "At the bottom i is %d" % i

            print "The numbers: "
            for num in numbers:
                print num

theloop(6,1)
