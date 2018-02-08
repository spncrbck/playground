import random

doors = 3
print("There are %s doors." % (doors))
availableDoors = list(range(1, doors + 1)) # build a list [1, 2, ..., n+1] of doors
prizeDoor = random.choice(availableDoors)
# print("Shhh. The prize door is %s." % prizeDoor)

selection = int(input("What door would you like to pick? ")) # user selects door

# here I built some overly complicated method of removing certain items from the list to use later
if selection == prizeDoor:
    availableDoors.remove(selection)
    removed = random.choice(availableDoors)
else:
    availableDoors.remove(selection)
    availableDoors.remove(prizeDoor)
    removed = availableDoors[0]

change = input("I'll remove door %s, would you like to change your selection? y/n " % (removed))
if change == "n" and selection != prizeDoor or change == "y" and selection != prizeDoor:
    print("Congratulations! You found the right door!")
elif change == "n" and selection != prizeDoor or change == "y" and selection == prizeDoor:
    print("Better luck next time! The correct door was %s!" % (prizeDoor))
else:
    print("I don't understand your input.")
    
"""
Future changes:
- Modify this so it really does work with any number of doors. As-is, this only works for three doors.
"""