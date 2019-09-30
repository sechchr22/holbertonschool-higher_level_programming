#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as valerr:
        print(valerr, file=sys.stderr)
        return False
    except TypeError as typeerr:
        print(typeerr, file=sys.stderr)
        return False
    else:
        return True
