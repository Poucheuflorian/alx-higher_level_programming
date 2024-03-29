#!/usr/bin/python3
"""This file contains a class Rectangle"""


class Rectangle():
    """ Real Class Resctangle """
    def __init__(self, width=0, height=0):
        if (type(width) != int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def __str__(self):
        if (self.__width == 0 or self.height == 0):
            return ''
        elif self.__height == 1:
            return self.__width * "#"

        else:
            str_width = self.__width * "#"
            string = ''
            for i in range(self.__height - 1):
                string = string + str_width + "\n"
            return string + str_width

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2*(self.__width + self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if (type(width) != int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    pass
