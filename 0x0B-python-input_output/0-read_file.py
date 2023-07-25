#!/usr/bin/python3
"""Write a function that reads a file and prints to STDOUT"""

def read_file(filename=""):
    """Reads a file filename
    Args: (filename)"""

    with open(filename, encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
