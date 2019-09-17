#!/bin/bin/python3
def print_list_integer(my_list=[]):
    for item in my_list:
        print("{:d}".format(item))


'''
Revisar que pasa si añado el
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
si no estoy mal esto es para que tanto funcione
como script tanto como en interactivo
'''
