#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as valerr:
        print("Exception: {}".format(valerr), file=sys.stderr)
        return False
    except TypeError as typeerr:
        print("Exception: {}".format(typeerr), file=sys.stderr)
        return False
