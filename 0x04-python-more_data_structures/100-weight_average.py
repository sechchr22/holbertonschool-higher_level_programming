#!/usr/bin/python3
def weight_average(my_list=[]):

    if len(my_list) == 0:
        return(0)

    num, denom = 0, 0
    mul = 1
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list[i])):
            mul *= my_list[i][j]
        num += mul
        mul = 1
        denom += my_list[i][len(my_list[i]) - 1]

    return(num / denom)
