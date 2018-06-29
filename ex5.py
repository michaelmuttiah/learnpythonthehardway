human_name = 'Zed A. Shaw'
human_age = 35 # not a lie
human_height = 74 # inches
human_height_cm = human_height * 2.54
human_weight = 180 # lbs
human_weight_kg = human_weight / 2.2
human_eyes = 'Blue'
human_teeth = 'White'
human_hair = 'Brown'

print "Lets talks about %s." % human_name
print "He's %d inches tall or %d cms tall ." % (human_height, human_height_cm)
print "He's %d pounds or %d kgs heavy" % (human_weight, human_weight_kg)
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (human_eyes, human_hair)
print "His teeth are usually %s depending on the coffee" % human_teeth

#this line is tricky try to get it right exactly
print "If I add %d, %d, and %d I get %d." % (
human_age, human_height, human_weight, human_age + human_height + human_weight)
