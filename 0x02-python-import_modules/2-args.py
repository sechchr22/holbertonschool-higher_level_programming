#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.". format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        if len(sys.argv) == 2:
            print("{:d} argument".format(len(sys.argv) - 1))
        elif i is 1:
            print("{:d} arguments".format(len(sys.argv) - 1))
        print("{:d}: {}".format(i, sys.argv[i]))
