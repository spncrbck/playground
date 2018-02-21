print("hello world")
intVal = 3
floatVal = 1.7
boolVal = True
print(boolVal)
boolVal = False
print(intVal)
print(floatVal)
print(boolVal)

# this is a single line comment

"""
This is a multiple-line comment.
Hella.
"""

"""

"""

# expressions
addition = 4 + 5
subtraction = 5 - 2
division = 10 / 2
exponentiation = 3 ** 3  # 3^3

# floor division operator - division without decimals
floorDiv1 = 16 // 3  # floorDiv = 5
floorDiv2 = 16 // 6  # floorDiv = 2

# modulo operator - finding remainer
modulo1 = 4 % 3  # modulo1 = 1 -- 3 goes into 4 with a remainder of 1
modulo2 = 17 % 3  # modulo2 = 2
modulo3 = 15 % 5 # modulo3 = 0

# assignment operator
addAssignment = 3
addAssignment += 5  # addAssignment = 8
# this means the same thing as
addAssignment = 3
addAssignment = addAssignment + 5
# this works for add, sub, mult, div, floor, exponentiation, modulo


str6 = "This is a string"

# escape sequences
str2 = "The book \"A Feast for Crows\" was written by George R. R. Martin"
print(str2)

# accessing characters within a string by index
str9 = "example"
ex1 = str9[0]  # assigns the variable ex1 "e"
ex2 = "tape"[2]  # assigns variable ex2 "p"


# string slicing allows you to get slices from a string and assign them to variables
example = "apples"
ex3 = example[:3]  # assign from beginning to one less than index; assign "app" to ex3
ex4 = example[2:5]  # from one index to one lower than another; assign "ple"
ex5 = example[3:]  # from index to end; assign "les"
# works the same as above if you want to assign straight from a string



# STRING METHODS

# length -- len()
string = "Yoda"  # we will use the len() method on this string
length = len(string)  # assigns the number of characters in the string "Yoda" to the variable length
print(length)  # prints 4

# str() string method -- allows you to change a number such as a float or integer to a string
num = 9  # we will use the str() method on this number
string = str(num)  # turns number 9 to "9" and assigns that string to the variable string
print(string)  # prints the string 9

# .lower() and .upper() string methods
str1 = "LOWER"  # will be changed from "LOWER" to "lower"
print(str1.lower())  # prints "lower" as output
str2 = "upper"  # will be changed from "upper" to "UPPER"
print(str2.upper())  # prints "UPPER" as output



# print() and string concatenation
print("word1" + "word2" + "word3")  # outputs string "word1 word2 word3"
print("R" + str(2) + "-D" + str(2))  # outputs string "R2-D2"

# the %s Format Operator
city = "Seattle"
state = "Washington"
# the line below prints the string "The Seahawks are from Seattle, Washington."
print("The Seahawks are from %s, %s." % (city, state))

# another print method including variables
testVar = 7
print('Here\'s how you include', testVar, 'variables inside a quote!')

# you can also print multiple things on the same line
print('Here is a caterpillar:')
print('o0O0' * 10)

# input
occupation = input("What is your occupation?")
city = input("What city do you live in?")
age = input("How many years old are you?")
print("You are a %s, you live in %s, and you are %s years old." % (occupation, city, age))


# flow control and comparators
# > and >= comparators
ex8 = 3 > 1 # ex8 = True
ex9 = 5 >=5 # ex9 = True
ex10 = 3 < 3 # ex10 = False
ex11 = 7 <= 6 # ex11 = False

# == (equal to) and != (not equal to) comparators
ex12 = 1 == 7 # ex12 = False
ex13 = 8 != 8 # ex13 = False


# Boolean operators - give a boolean value based on a comparison of statements
# 'and' Boolean operator
ex14 = True and True # ex14 = True
ex15 = True and False # ex15 = False
ex16 = False and False # ex16 = False

# 'or' BO
ex17 = True or True # True
ex18 = True or False # True
ex19 = False or False # False

# 'not' BO
ex20 = not True # False
ex21 = not False # True

# order of operations for boolean operators - not, and, or
ex22 = not False and not True or False
step1 = True and False or False
step2 = False or False
result = False


# if, else, and elif
# if statments
if 5!= 6:
    print("5 does not equal 6") # must be indented 4 spaces or a multiple of 4 spaces

# else statements
if 1 == 2:
    print ("1 equals 2")
else:
    print ("1 does not equal 2")

# elif statements - run if none of the above if/else statements execute their code and the elif statement = True
if 1 == 2:
    print("Don't print this.")
elif 1 != 2:
    print("Print this.")
else:
    print("Don't print this either.")
# you can have any number of elif statements between if/else statements
# works kind of like a coin sorter


# FUNCTIONS
# defining and calling functions with no parameters
def function1():
    print("hello world")
function1()

# defining and calling functions with a single parameter
def single(a):
    print(a)
single(a)

# test:
def echo(spoken):
    print(spoken)
spoken = input("Speak to the cave. ")
echo(spoken)

# defining and calling functions with multiple parameters
def mult(a, b, c):
    d = a * b
    print(d + c)
mult(2, 3, 4)
# outputs (a * b) + c -> (2 * 3) + 4 -> 10

# calling functions inside of other functions
def giver(a, b):
    c = a + b
    return c
def taker(d, e):
    output = giver(d, e) # c is assigned to the function 'output' using 'giver'
    return output
print(taker(1, 5)) # calls giver with 1 and 5 and assigns it to 6, then prints 6


# importing modules - contain sets of functions
# generic imnport
import random # module that lets you create random things
print(random.randint(1,10)) # randint takes two parameters >= or <= to each number

# import specific functions from a module
from random import randint
print(randint(10,20))

# universal import - import every function from a module
from random import *
print(random()) # returns a floating point number equal to or between 0.0 and 1.0


# built-in functions in python
# abs() - absolute value
ex23 = abs(-3) # ex23 is assigned to 3

# type() determines type of input
ex24 = type(1) # returns type of value -> int
ex25 = type(3.21) # float
ex26 = type("example") # string
ex27 = type(True) # bool

# max() can take any number of inputs between parentheses, but must all be same type of input
ex28 = max(3, 9, 7, 13) # ex28 assigned to 13
ex29 = max("a", "b", "t", "z") # ex29 assigned to z
ex30 = max("az", "ab", "az") # az
# also works for floating point values

# min() does the same as max() but the opposite
ex31 = min(11, 3, 9, 10) # ex31 assigned to 3


# LISTS (data type)
# list is a data type that can be used to assign a collection of values to a single variable
# listForm = [first, second, third, etc]
example1 = ["eggs", 1, "spam", 7.96]
example2 = [] # can also be empty

# accessing by index
byIndex = ["green", "eggs", "and", "ham"]
ham = byIndex[3] # ham
greenEggs = byIndex[0] + " " + byIndex[1] # green eggs

# index re-assignment
reAssign = [1, 1, 3, 8]
reAssign[2] = 5 # re-assigns reAssign[2] to the value of 5
# now, reAssign = [1, 1, 5, 8]

# .append() - adds item to the end of a list
# nameOfList.append(value)
adder = [1, 2, 3, 4]
adder.append(5) # appends 5 to the end of adder
# now, adder = [1, 2, 3, 4, 5]

# list slicing
sliceEx = [9, 0, 2, 1, 0]
slice1 = sliceEx[:2] # slice1 = [9, 0]
slice2 = sliceEx[2:4] # slice2 = [2, 1]
slice3 = sliceEx[1:] # slice3 = [0, 2, 1, 0]

# .index() -  used to search for and return the index of the first time a value appears in a list
indexed = [0, 1, 0, 1, 1]
firstZero = indexed.index(0) # firstZero = 0

# .insert() = used to add an item to a list anywhere
inserted = ["Through", "Looking", "Glass"]
inserted.insert(1, "the") # inserts "the" at index 1 of inserted
# now, inserted = ["Through", "the", "Looking", "Glass"]

# .remove() - remove a single item from a list
theStarks = ["Ned Stark", "Catelyn Stark", "Tony Stark", "Bran Stark"]
theStarks.remove("Tony Stark")

# .pop() - used to remove and return an item from a list based on its index
ironMan = theStarks.pop(2)
# removed index 2 (Tony Stark) from the 'removed' list and assigned it to value ironMan


# For loops and Tuples
# tuple - data type like lists, contain values
# unlike lists - they are immutable - their contents cannot be modified
tuple1 = 1, 5.2, True, "Yes"
tuple2 = (2, False, "hello", 7.24)
empTup = () # empty tuple

# accessing values by index and slicing for tuples
tupEx = (1, 2, 3, 4, 5)
print(tupEx[1]) # prints 2
print(tupEx[3]) # prints 4
first3 = tupEx[:3] # first3 assigned to (1, 2, 3)
mid3 = tupEx[1:4] # mid3 assigned to (2, 3, 4)
last3 = tupEx[2:] # last3 assigned to (3, 4, 5)


# FOR LOOPS - do something with every item with a piece of data that has indexes
list1 = [1, 2, 3]
tuple3 = (4, 5, 6)
# iterate through list:
for elements in list1:
    print(elements)
# iterate through tuple:
for items in tuple3:
    print(items)

# using for loops to work with lists and strings
listy = [4, 3, 2, 1, 0]
empty = []
tup = ("Let", "It", "Be")
song = ""
for nums in listy:
    empty.append(nums * 4)
# now, empty = [16, 12, 8, 4, 0]
for words in tup:
    song += words
# now, song = "Let It Be"
print(empty)
print(song)


# DICTIONARIES
# dictionary - data type in python like a list, but instead of indexes, it has keys
# keys in dictionaries - can be any string or number while indexes are always the same
states = {42: "Washington", 50: "Hawaii", 1: "Delaware"}
print(states[42]) # prints Washington
print(states[50]) # prints Hawaii
print(states[1]) # prints Delaware

# empty dictionaries, adding to dictionaries, and length of dictionary
Dict = {} # empty dictionary
Dict[30] = "Wisconsin" # adds the key 30 and value "Wisconsin" to dictionary Dict
Dict[21] = "Illinois"
lenOfDict = len(Dict) # lenOfDict = 2

# re-Assignment by key
moreStates = {10: "Virginia", 15: "Kentucky", 48: "New Mexico"}
moreStates[48] = "Arizona"
# now, moreStates = {10: "Virginia", 15: "Kentucky", 48: "Arizona"}

# removing key/value pairs using Del
del moreStates[10]
# now, moreStates = {15: "Kentucky", 48: "Arizona"}


# USING FUNCTIONS WITH LISTS
# passing a list to a function
exList = ["pass", "this", "list", "to", "a", "function"]
def list_passer(li):
    return li
print(list_passer(exList))
print(list_passer([1, 2, 3]))

# accessing an element in a list using a function
exList2 = [9, 0, 2, 1, 0]
def list_accessor(li):
    return li[3]
print(list_accessor(exList2)) # prints 1

# modifying a list element within a function
def list_modifier(li):
    return li[2] / 0.5
print(list_modifier(exList2)) # prints 4.0

# manipulating lists within functions
# can use append, insert, pop, remove, etc...
exList3 = [1, 1, 3, 8]
def list_manip(li):
    li.remove(3) # 3 is removed from list
    li.insert(2, 4) # 4 is inserted at 2nd index
    return li
print(list_manip(exList3)) # prints [1, 1, 4, 8]

# using an entire list within a function
# printing a list's elements using a for loop within a function
exList4 = [1, 2, 3, 4, 5]
def print_items(a):
    for items in a:
        print(items)
print_items(exList4)
"""
output looks like
1
2
3
4
5
"""

# range() - function that is useful for easily creating lists
# range(stop)
var1 = range(8) # [0, 1, 2, 3, 4, 5, 6, 7]
# range(start, stop)
var2 = range(1, 4) # [1, 2, 3]
# range(start, stop, step)
var3 = range(2, 20, 3) # [2, 5, 8, 11, 14, 17]
# lists generated are immutable

# passing a list made using range() into a function
# range(stop)
var4 = range(5) # [0, 1, 2, 3, 4]
def passed(x):
    return(x)
print(passed(var4)) # prints range(0, 5)

# can be useful using in a for loop to iterate through a list of *unknown* or *varying length*
exList5 = [1, 5, 9, 13]
def iterator(a):
    for x in range(0, len(a)):
        print(a[x])
iterator(exList5)
"""
output looks like
1
5
9
13
"""

# modifying elements from a list using range()
exList6 = [1, 33, 5, 7, 9]
def modifier(a):
    for item in range (0, len(a)):
        a[item] *= 2
    return a
print(modifier(exList6)) # prints [2, 6, 10, 14, 18]

# passing multiple lists into a function
list1 = [1, 3, 5]
list2 = [2, 4, 6]
def multiList(a, b):
    print(a, b)
multiList(list1, list2)

# how to iterate through a list comprised of other lists
listOfLists = [[1, 3, 4], [2, 5, 6]]
def makeOneList(a):
    bothLists = []
    for item in a:
        for element in item:
            bothLists.append(element)
    print(bothLists)
makeOneList(listOfLists) # prints [1, 3, 4, 2, 5, 6]
