#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list
    """
    for i in range(x):
        try:
           print( my_list[i],end = "")
        except IndexError:
            return i
    return x

if __name__ == '__main__':
    print(safe_print_list([1,2,3],5))
