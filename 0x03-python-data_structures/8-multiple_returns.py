#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        new_tuple = (0, None)
        return(new_tuple)
    else:
        new_tuple = (len(sentence), sentence[0])
        return(new_tuple)
