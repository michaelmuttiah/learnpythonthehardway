def addition (a,b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some maths with just functions\n"

age = addition(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "\nAge: %d, Height: %d, Weight: %d, IQ: %d\n" % (age, height, weight, iq)

# A puzzle for the extra credit

print "Here is a puzzle."

what = addition(age, subtract(height, multiply(weight, divide(iq, 2))))

print "\n That formula seems a bit complicated lets simplify it.\n"

# Steps for Calculation
# 50 / 2
# 180 * 25
# 74 - 4500
# 35 + -4426
# = -4391

# Part 2 - Simplify the function

A = 50
B = divide(A, 2)
C = multiply(180, B)
D = subtract(74 , C)
E = addition(35, D)

print "\n So what is the result?\n"

Formula = E

print " So the above formula simplified is", Formula

print "\n OK, lets much around with our functions \n"

def add (a,b):
    print "ADDING %d + %d" % (a, b)
    return a + a + b

def sub (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b - a

def mul (a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b * b * a

def div (a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b / b

A = 50
B = div(A, 2)
C = mul(180, B)
D = sub(74 , C)
E = add(35, D)

print " \nSo our new result would be\n", E,

#Part 3 , Do the sum from Part 1 Backwards

def add (a,b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def sub (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def mul (a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def div (a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

A = div(50, 2)
B = mul(180, A)
C = sub(74 , B)
D = add(35, C)

print " \nSo our new result would be\n", E,

#Part 3 , Do the sum from Part 1 Backwards

what2 = div(A, mul(B ,sub(C ,add(D, 2))))

print " \nSo Part 3 backwards is\n ", what2,
