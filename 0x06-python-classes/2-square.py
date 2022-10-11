#!/usr/bin/python3
"""A class Square that defines a square by
Private instance attribute: size"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Validates is size is an integer
            and not less than zero """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
