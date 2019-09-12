#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    module = abs(number) % 10
else:
    module = number % 10

str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"

if number > 9 or number < -9:
    if module == 0:
        print("Last digit of {} is {} {}".format(number, module, str2))
    elif number < 6:
        if number < 0:
            print("Last digit of {} is -{} {}".format(number, module, str3))
        else:
            print("Last digit of {} is {} {}".format(number, module, str3))
    else:
        print("Last digit of {} is {} {}".format(number, module, str1))

elif number is 0:
    print("Last digit of {} is 0 {}".format(number, str2))

else:
    if number > 5:
        print("Last digit of {} is {} {}".format(number, number, str1))
    else:
        print("Last digit of {} is {} {}".format(number, number, str3))
