#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    div = 0
    my_list_3 = []
    while (i < list_length):
        try:
            div = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except ValueError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            my_list_3.append(div)
            div = 0
            i += 1
    return(my_list_3)
