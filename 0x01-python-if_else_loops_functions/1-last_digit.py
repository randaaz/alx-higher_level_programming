#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_of_number = number % 10 if number > 10 else number % -10
if (last_digit_of_number > 5):
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_digit_of_number))
elif (last_digit_of_number == 0):
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, last_digit_of_number))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit_of_number))
