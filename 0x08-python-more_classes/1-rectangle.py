#!/usr/bin/python3
"""A class that defines a rectangle 
by hight and width
"""


class Rectangle:
    """Instantiate an instance with 
    defualt values of width and height
    """
    
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """set getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set new value for width"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """set getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """set new value for height"""
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
