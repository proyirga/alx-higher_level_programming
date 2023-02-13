#!/usr/bin/python3
"""A class that defines a square by size."""


class Square:
    """Initiate the  square class"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculate area of the square
        Return: area
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
