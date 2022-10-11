#!/usr/bin/python3
"""A class Square that defines a square by size"""


class Square:
    """Initializing this class"""

    def __init__(self, size=0):
        """Validating size attribute is an
        integer and not less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square
        """

        return (self.__size * self.__size)
