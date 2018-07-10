from sys import exit

p = "> "

def wizard():

def fruit():

def cottage():
    print "You see the goblins were guarding a cottage."
    print "It looks abandoned."
    print "What do you do?"

    next = raw_input(p)

    if "enter" in next:
        print "The door creeks open. Inside there is a table with a fresh bowl of fruit."
        def fruit():
    elif "walk" in next:
        print "Ahead of you, you see another cottage with smoke coming out."
        def wizard():
    else:
        "You can't do that."
        cottage()

def forest():
    print "You find yourself back in the forest. Where do you go?"

    next = raw_input(p)

    if next == "north":
        mountains()
    elif next == "east":
        hills()
    elif next == "west":
        lake()
    else:
        print "Hmmm. Nothing there. Try another way."
        start()

def mountain_fight():
    print "You walk towards a cowering robed figure."
    print "As you get closer, 3 goblins appear from the trees laughing."
    print "They all have swords."
    print "What do you do?"

    next = raw_input(p)

    if "fight" in next :
        print "Do you have a sword?"
            next = raw_input(p)
            if "yes" in next:
                print "You kill one of the goblins and the rest flee."
                cottage()
            else:
                print " You crazy mofo, you have no weapons"
                die()
    elif "run" in next:
        print "Probably a good idea"
        forest()
    else:
        "Too slow."
        die()

def mountains():
    print "You find yourself walking up to the mountains."
    print "The path is steep and you can hear someone shouting for help."
    print "What do you do?"

    next = raw_input(p)

    if next == "help":
        mountain_fight()
    elif next == "keep walking":
        cottage()
    else:
        "Hmm. Try again."
        mountains()

def halls():

def dragon():

def princess():

def end():

def hills():

def lake_riddle():
    print """ If you can answer my riddle in 3 goes or less.
    I will give you a mighty weapon, to help on your quest.

    What is greater than God,
    more evil than the devil,
    the poor have it,
    the rich need it,
    and if you eat it, you'll die?

"""
    answer = "nothing"
    tries = 0
    tries_remaining = 3

    while tries < 3:
        try:
            guess = raw_input("What is your guess? > ")
            tries += 1
            tries_remaining -= 1

            if "nothing" in answer:
                print "Correct! I bestow upon you this mighty sword to cleave through your enemies"
                forest()
            else:
                print "Incorrect! Tries remaining: %d" % tries_remaining
                continue
        except ValueError:
            tries += 1
            tries_remaining -= 1
            print "That is not an option. The genie penalizes you a try. Be careful!"
            print "Tries remaining: %d" % tries_remaining

    if "nothing" in answer:
        print "Correct! I bestow upon you this mighty sword to cleave through your enemies"
        forest()
    else:
        die("The figure cuts you in a half with a sword of water.")

def lake():
    print "You come across a beautiful lake as far as the eye can see."
    print "Suddenly the waters churn and a figure rises from the water."
    print "Why have you come here? His voice booms."

    next = raw_input(p)

    if "princess" in next:
        print "The figure smiles and says 'Perhaps I can help you on your quest' "
        lake_riddle()
    else:
        "'You dare to disturb me!' The figure cuts you in half with a sword of water'"
        die()

def die(you):
    print "You died, better luck next time."
    start()

def start ():
    print " Welcome to the text based game: Princess of Fire."
    print "Your aim is to find and rescue the princess."
    print "You come to in a forest which way do you go?"

    next = raw_input(p)

    if next == "north":
        mountains()
    elif next == "east":
        hills()
    elif next == "west":
        lake()
    else:
        print "Hmmm. Nothing there. Try another way."
        start()

start()
