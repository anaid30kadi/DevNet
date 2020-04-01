"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print ("El valor de pi es:", pi) #Method 1
printpi = ("El valor de pi es: {}".format(pi)) #Method 2
print (printpi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if i < 50:
    print (i,"is less than 50")
elif i > 50:
    print (i,"is greather than 50")
else:
    print (i,"is equal to 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'lemon', 'banana'])

if picked_fruit == 'orange':
    color = "orange"
    print ("Your fruit is an {} an its color is {}".format(picked_fruit,color))
elif picked_fruit == 'lemon':
    color = "green"
    print ("Your fruit is an {} an its color is {}".format(picked_fruit,color))
else: 
    color = "yellow"
    print ("Your fruit is an {} an its color is {}".format(picked_fruit,color))  


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

i = random.randint(0, 100)
n = random.randint(0, 100)

def multiplier (num1,num2):
    result = num1 * num2
    return result

print ("The ramdom multiplier result is:", multiplier (i,n))


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiplier(12,96))

print("48 x 17 =",multiplier(48,17))

print("196523 x 87323 =",multiplier(196523,87323))

