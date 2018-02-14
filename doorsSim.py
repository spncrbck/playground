import random
 
availableDoors = [1, 2, 3]
wonChange = wonKeep = lostChange = lostKeep = 0
 
trials = 10000
trialsCompleted = 1
 
while trialsCompleted <= trials:
    prizeDoor = random.choice(availableDoors)
    selection = random.choice(availableDoors)
    change = bool(random.getrandbits(1))
    if selection == prizeDoor and change == False:
        wonKeep = wonKeep + 1
    elif selection != prizeDoor and change == True:
        wonChange = wonChange + 1
    elif selection != prizeDoor and change == False:
        lostKeep = lostKeep + 1
    elif selection == prizeDoor and change == True:
        lostChange = lostChange + 1
    else:
        break
    trialsCompleted = trialsCompleted + 1
 
print("%s trials were run." % (trials))
print("Keeping selection won %s games and lost %s." % (wonKeep, lostKeep))
print("Changing selection won %s games and lost %s." % (wonChange, lostChange))