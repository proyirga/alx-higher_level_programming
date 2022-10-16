#!/usr/bin/python3
"""0-add_integer module supplies one function, add_integer(a, b)
which adds two integers."""


def add_integer(a, b=98):
    """adds 2 integers.
    a and b must be integers or floats,
    otherwise raise a TypeError exception 
    with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float

    Return: an integer: the addition of a and b
    """

    if not isinstance(int, a) or not isinstance(int, b):
        raise TypeError("a must be an integer")
    if not isinstance(float, a) or not isinstance(float, b):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
