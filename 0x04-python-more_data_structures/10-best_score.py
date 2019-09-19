#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return(None)
    elif len(a_dictionary) is 0:
        return(None)
    list_a_dictionary = []
    for key in a_dictionary:
        list_a_dictionary.append(a_dictionary[key])
    list_a_dictionary.sort()
    for key in a_dictionary:
        if a_dictionary[key] is list_a_dictionary[len(a_dictionary) - 1]:
            return(key)
