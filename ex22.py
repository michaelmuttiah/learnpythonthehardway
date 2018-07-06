# Summary of terms learnt from lessons 1 - 21

1. print "" # prints a string in speech marks, can us single or double
2. # #allows you to comment a code, this is not run in the script
3. float() # designate a number as being able to have decimal points
4. cars = 7 # this is a variable, when put into print it will print the variable
            # value which is assigned to it
         # that has been assigned to it i.e. print "How many cars are there?", cars
5. # printing variables
my_name = 'Mike'
print "Let's talk about %s." % my_name
# Above I have assined the variable my_name a value, then put it into a string
# Its place is denoted by %s which points to the # variable name outside the string
6. %d = number, %s = string %r = displays raw data, also used in debugging
7. hilarious = True , hilarious = False #(Example of Boolean Values i.e. 1 or 0
# true of false)
8. print """ #Can be used to print a long string over multiple lines and then
closed again using """ without have to type print "" everyline
9. print "\n" #Put at start or end of print to print on a new line
10. print "\t*" #Prints Tabbed in like>      this
11. print "How old are you?"
age = raw input()
# Raw input allows the user to input a variale value
12. print "So you're %r old, %r tall and %r heavy " (age, height, weight)
# This is how we print multiple variable Values
13. from sys import argv # from a library (sys) we are importing a variable/module
# (argv) stands for argument variable
14. script, user_name = argv # Here we are asking to 2 items or information
# to be inputted prior to running the programme in terminal
# i.e. we would say python ex22.py (script) Mike (name being used in script)
15. prompt = '> ' # when asking a user for raw input, you would ask for a prompt
# asking them to enter the information. This assigns the variable a printed
# output
16. script, filename = argv
txt = open(filename) # the above is assigning variables to argv, which means
# the assigns a file to the script (a txt file) then open (filename)
# opens the filename
17. print txt.read() # reads the file and prints it on the terminal
18. close # Closes the file i.e. target.close() whether target is assined as
# target = open(filename, "w") the "w" makes it writeable
19. read # reads the filename
20. readline # reads one line of the text filename
21. truncate # empties the file (deletes it)
22. write(stuff) #writes text to the filename
23. from os.path import exists #another command exists which returns a True
# statement is a file exists that we are calling
24. script, from_file, to_file = argv # we assign 3 values to the variables
# as this is part of a script to write text from one file to another
< Chapter 17> 
