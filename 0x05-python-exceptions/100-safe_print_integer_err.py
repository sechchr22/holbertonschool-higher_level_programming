#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as valerr:
        print("{}".format(valerr), file=sys.stderr)
        return False
    except TypeError as typeerr:
        print("{}".format(typeerr), file=sys.stderr)
        return False
    else:
        return True
