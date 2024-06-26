#!/usr/bin/python3

"""First definition of a class Rectangle
First definition of a class Rectangle
"""


class Rectangle():
    """Write a class Rectangle that defines a rectangle by:
(based on 8-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception
with the message width must be an integer
if width is less than 0, raise a ValueError exception w
ith the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception
with the message height must be an integer
if height is less than 0, raise a ValueError exception
with the message height must be >= 0
Public class attribute number_of_instances:
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
Public class attribute print_symbol:
Initialized to #
Used as symbol for string representation
Can be any type
Instantiation with optional width and height
: def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self):
that returns the rectangle perimeter:
if width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #:
if width or height is equal to 0, return an empty string
repr() should return a string representation of the rectangle to be able
to recreate a new instance by using eval()
Print the message Bye rectangle...
(... being 3 dots not ellipsis) when an instance of Rectangle is deleted
Static method def bigger_or_equal(rect_1, rect_2):
that returns the biggest rectangle based on the area
rect_1 must be an instance of Rectangle,
otherwise raise a TypeError exception with the
message rect_1 must be an instance of Rectangle
rect_2 must be an instance of Rectangle,
otherwise raise a TypeError exception with
the message rect_2 must be an instance of Rectangle
Returns rect_1 if both have the same area value
Class method def square(cls, size=0)
: that returns a new Rectangle instance with width == height == size
You are not allowed to import any module
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height - 1):
                string = string + self.__width * Rectangle.print_symbol + '\n'
            return string + self.__width * Rectangle.print_symbol

    def __repr__(self):
        return "Rectangle({},{})".format(self.__width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 0 if (self.__width == 0 or self.height == 0)\
                else 2 * (self.__width + self.__height)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2
