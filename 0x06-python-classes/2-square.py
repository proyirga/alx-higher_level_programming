#!/user/bin/python3
"""A class Square that defines a square by
Private instance attribute: size"""


class Square:
    """Instantiation with optional size"""
    def __init__(self, size=0):
        """Validate that size is an integer
        and not less than 0"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
