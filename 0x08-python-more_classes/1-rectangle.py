#!/usr/bin/python3
"""A class that defines a rectangle by hight and width"""


class Rectangle:
    """Instantiate an instance with defualt values
    of width and height
    """

    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height
    
    #set getter for width
    @property
    def width(self):
        return self.__width

    #set new value for width
    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")


    #set getter for height
    @property
    def height(self):
        return self.__height
    
    #set new value for height
    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
