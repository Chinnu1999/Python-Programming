# Python Programming
# Day-4

# Randomization - (Random Module)

# printing random integers
import random  # ->  it a module used to print random things
random_integer = random.randint(1, 10)  # -> printing random number using randint[random integers]
print(random_integer)

# printing random float number
import random
random_float = random.random() # random() will print between 0.00000000 - 0.999999999.....
print(random_float)

# printing random decimal number
import random
random_decimal = random.uniform(0,5) 
print(random_decimal)
                      # (or)
import random
random_float = random.random()*5
print(random_float)

#--------------------------------------------------------------------------------------------

# we can generate random love score calculator

import random
love_score=random.randint(1,100)
print(f"Your love score is {love_score}. ")

#--------------------------------------------------------------------------------------------

# Excercise - 1

# Head or Tail Exercise

import random
test_seed = input("Create a number for head or tail: ")  # seed will get one number from user as input
random.seed(test_seed)
random_side = random.randint(0,1) # randomly it assign whether o or 1 if they as 0 for user input we get tail or it randomly assign 1 we get head
if random_side == 1:
  print("Head")
else:
  print("Tail")


#-----------------------------------------------------------------------

# Lists

country = ['india', 'america', 'singapore', 'china', 'italy'] # creating Lists
print(country[0])  # printing index 0 from the variable country
#       (or)
print(country)

# we can change the items in list
country[3] = 'iran'
print(country)

# append - add any item to the end of the list
country.append('Iraq')     #append takes exactly one arguments
print(country)

# extend - add bunch of items with in the square bracket at the end of lists 
country.extend(['pakistan', 'korea', 'south-korea'])
print(country)

# split - what split actually do?  - provide some value and assign variable name
name1 = ("chinnu, john, harry")
print(name1.split())    # its will make a list we provide in the name1 variable

#------------------------------------------------------------------------------------------------------------------------

# Excercise - 2 
# Hotel random food pay

#You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Answer:

import random
name = input("Enter all your friends name here: ") # getting input from user
name1 = name.split(", ")                           # all names are split into lists
length = len(name1)                                # checking the names length
person_length = random.randint(0, length - 1)      # randomly choosen the index from 0 to n-1
rand_name = name[person_length]                    # print the name that choosen from index(randomly)
print(f"{rand_name} is going to buy a meal today!......")

#----------------------------------------------------------------------------------------------------------------------

# Index Error  with Nested List

states_of_india = ["Tamilnadu", "Karnataka", "Kerela", "Mumbai", "Delhi"]

india = len(states_of_india)
print(states_of_india[india -1])

#---------------------------------------------------------------------------------------------

# Excercise - 3

# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']


# Treasure Map Excercise

row1 = ["⬜️","⬜️","⬜️"]                                   # row 1
row2 = ["⬜️","⬜️","⬜️"]                                   # row 2
row3 = ["⬜️","⬜️","⬜"]                                   # row 3
map = [row1, row2, row3]                                    # 3 rows combined inside the variable named map
print(f"{row1}\n{row2}\n{row3}")                            # \n printing 3 rows line by line 
position = input("Where do you want to put the treasure? ") # enter the position where you want to put like 23....
horizontal = int(position[0])                               # if you enter 23 the horizontal position will take 2
vertical = int(position[1])                                 # if you enter 23 the vertical position will take 3
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

#----------------------------------------------------------------------------------------------------------------------
