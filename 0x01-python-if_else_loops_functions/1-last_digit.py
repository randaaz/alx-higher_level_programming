#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_of_number = number % 10 if number > 10 else number % -10
 print("Last digit of {:d} is {:d} and is ".format(number, last_digit_of_number, end=""))
if (last_digit_of_number > 5):
    print("greater than 5")
elif (last_digit_of_number == 0):
    print("0")
else:
    print("less than 6 and not 0")
