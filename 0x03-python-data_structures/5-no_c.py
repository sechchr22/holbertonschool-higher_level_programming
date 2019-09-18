#!/urs/bin/python3
def no_c(my_string):

    ls = list(my_string)

    for i in range(0, len(my_string)):
        if ls[i] == 'C' or ls[i] == 'c':
            ls[i] = ""

    return(''.join(ls))
