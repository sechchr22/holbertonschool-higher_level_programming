#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    str = dir(hidden_4)
    for string in str:
        if string[0] != "_":
            print("{}".format(string))
