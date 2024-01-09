#!/usr/bin/python3
"""
This module contains one class
the name is Square
"""
class Square():
    """
    This is an empty class named Square.
    it will be the first class of our journey in alx with python
    """
    def __init__(self,size):
        """ This init function instatiate a square objet wit a private attribut called size with the value size """

        self.__size = size
    pass

if __name__ == "__main__":
    print("hello Square")
