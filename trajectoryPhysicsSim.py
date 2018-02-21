from math import *
from time import sleep
from termcolor import colored

decimalPlaces = 2
acceleration = -9.81 # gravitational constant = acceleration

def newLine():
    return print("")
def introduction():
    print(colored("Welcome to spncrbck's Basic Trajectory Calculator.", 'white', attrs=['bold', 'underline']))
    sleep(2)
    newLine()
    print("Based on input values for the angle of trajectory and initial velocity, this program will calculate information regarding final velocity, distance traveled, and more.")
    sleep(4)
    newLine()
    viewReadMe = str(input(colored("Would you like to read more about the assumptions made in these calculations? y/n ", 'magenta')))
    if viewReadMe == "y":
        newLine()
        readMe()
    elif viewReadMe == "n":
        newLine()
        print("Enjoy this project!")
        newLine()
        newLine()
    else:
        print("Since I didn't understand your input, I'll just continue to the project. Enjoy!")
        sleep(1)
        newLine()
        newLine()
def readMe():
    print(colored("Begin README.", 'white', attrs=['bold', 'underline']))
    sleep(1)
    newLine()
    print("As you may understand, this is a simple python project to do some basic trajectory calculations. Without making some assumptions, this calculation would be much more complex and defeats the purpose of a 'simple python project.'")
    sleep(5)
    newLine()
    print("Some assumptions being made are:")
    print("- no wind/air resistance")
    print("- perfectly level 'ground'")
    print("- uniform gravitational field with a gravitational constant of g = -9.81 m*s^-2")
    print("(in the future, I'd like to be able to have a setting in the begging of this program to choose the heavenly body from which this calculation is made)")
    print("- among other things")
    sleep(8)
    newLine()
    newLine()
def cosine(a): # cos(90) -> ~0 (must use round function to fix ridiculous output)
    return cos(radians(a))
def sine(a): # sin(90) -> ~1 (use round function)
    return sin(radians(a))
def roundIt(a): # rounds input of 'a' to the set number of decimal places
    return round(a, decimalPlaces)
def simulate():
    print(colored("Shooting trajectory!", 'red', attrs=['bold']))
    sleep(timeToPeak)
    print(colored("Trajectory at max height!", 'red', attrs=['bold']))
    sleep(timeToPeak)
    print(colored("Trajectory has hit the ground!", 'red', attrs=['bold']))
    sleep(5)
    print("...heh... I didn't tell you that the only dimension in which this simulation would run is time!")
    sleep(4)
    newLine()
    newLine()

introduction()
print("The program will now gather your initial constraints.")
sleep(2)
newLine()
theta = int(input(colored("Measured positively from the horizon, what is the angle of the shot in degrees? Please choose an integer between 1 and 90. ", 'magenta')))
newLine()
vI = int(input(colored("In meters-per-second (m/s), What is the initial velocity of the projectile? ", 'magenta')))
newLine()
print(colored("Crunching numbers!", 'red'))
newLine()

# need to splice trajectory and velocity components to get x- and y-dependent initial velocity
vIx = roundIt(vI * cosine(theta))
vFx = vIx # initial and final horizontal velocity is the same since we are assuming no wind resistance
vIy = roundIt(vI * sine(theta))
vFy = 0 # zero final vertical velocity
timeToPeak = roundIt( (1 / acceleration) * (vFy - vIy) ) # using (3) rearranged to (i)
maxElevation = roundIt( (1 / (2 * -(acceleration)) ) * (vFy - vIy) ** 2) # set (i) = (ii) and solve for d. call this (iii)
flightTime = roundIt(timeToPeak * 2) # in perfect conditions, something accelerates as quick as it decelerates
maxDistance = roundIt( 0.5 * (vIx + vFx) * flightTime ) # (4)

print("The x and y components of the initial velocity are, respectively, [%s, %s] (m*s^-2)" % (vIx, vIy))
sleep(2)
newLine()
print(colored("The trajectory reached its maximum elevation of %s meters in %s seconds." % (maxElevation, timeToPeak), 'cyan'))
sleep(2)
newLine()
print(colored("The trajectory took %s seconds to reach a distance of %s meters." % (flightTime, maxDistance), 'cyan'))
sleep(4)
newLine()
showRealTime = input(colored("Would you like to visualize this trajectory in one dimension? y/n ", 'magenta'))
newLine()
if showRealTime == 'y':
    simulate()
elif showRealTime == 'n':
    newLine()
    newLine()
else:
    print("Sorry, I didn't understand that. I'll assume you meant 'no'.")
    sleep(3)
    newLine()
    newLine()
print(colored("Thank you for trying this basic calculator out!", 'cyan', attrs=['bold']))
