#!/usr/bin/python3
# 1-square.py
"""A Square class that defines a square based:
Private instance attribute: size
Instantiation with size (no type/value verification)."""


class Square:
    """Square"""
    def __init__(self, size):
        """Initialize class"""
        self.__size = size
