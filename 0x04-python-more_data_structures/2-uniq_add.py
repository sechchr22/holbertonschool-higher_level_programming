#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    unique = set(my_list)
    my_list_unique = list(unique)
    for i in range(0, len(my_list_unique)):
        suma += my_list_unique[i]
    return(suma)
