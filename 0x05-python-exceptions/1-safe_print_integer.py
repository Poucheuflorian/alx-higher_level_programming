#!/usr/bin/python3

def safe_print_integer(value):
    """Write a function that prints an integer with "{:d}".format()"""
    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError):
        return False
    return True
