#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as valerr:
        print(valerr)
        return False
    except TypeError as typeerr:
        print(typeerr)
        return False
    else:
        return True
