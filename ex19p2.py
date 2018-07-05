def fruit_salad (fruit_count, bowl_count):
    print "You have %d pieces of fruit." % fruit_count
    print "You have %d bowls." % bowl_count
    print "That's alot of fruit!"
    print "Let'see if the neighbours want some. :)"

print "Give the number's directly" #1
fruit_salad (30,30)

print "Set new variables in the script" #2
amount_of_fruit = 20
amount_of_bowls = 20

fruit_salad(amount_of_fruit, amount_of_bowls)

fruit_salad( 6 * 5, 4 + 8) #3

fruit_salad ( amount_of_fruit + 20, amount_of_bowls - 5) #4

print "Let's ask the user to input instead" #5

print "How many pieces of fruit do you have?"
fruit_count = raw_input()

print 'How many bowls do you have?'
bowl_count = raw_input()

fruit_salad(amount_of_fruit, amount_of_bowls)
