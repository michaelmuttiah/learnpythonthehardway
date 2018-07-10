from sys import exit

#The last room is defined first, as it is referred to in later function

#Goblin room is mine, ridiculously happy at building my first simple text game
#and finally understading the structure and all the function

def goblin_room():
    print "You fall through a hatch into a bale of hay, you are in a large hall."
    print "You can see Goblin eating wolf meat at a table in the corner"
    print "What do you do?"

    next = raw_input("> ")

    if next == "attack goblins":
        print "You just got fucked..."
        dead("Who attacks a table full of goblins?")
    elif next == "look for a door":
        print "You see a tall oak door behind you"
    else:
        print "The goblins hear you crunching around in the hay."

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        print "Too much! The floor boards give way."
        goblin_room()


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got not idea what that means."


def ctulhu_room():
    print "Here you see the great evil Ctulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        ctulhu_room()

def dead(why):
    print why, "You died!"
    exit(0)

# I found it funny that the start function is at the end of the code

def start():
    print "You are in a dark room."
    print "There us a door to your right and left"
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        ctulhu_room()
    else:
        dead("You stumble around until you starve.")

start()
