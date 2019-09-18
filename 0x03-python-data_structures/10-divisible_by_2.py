#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if my_list is None:
        return(None)

    true_or_false = []

    for i in my_list:
        if my_list[i] % 2 == 0:
            true_or_false.append(True)
        else:
            true_or_false.append(False)

    return(true_or_false)
