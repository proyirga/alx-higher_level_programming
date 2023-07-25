#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
and returns the number of characters written:"""


def write_file(filename="", text=""):
    """write a string to a text file
    Args: 
        filename: name of the file
        text: strings to be written to a file filename
    """ 

    with open(filename, "w", encoding="UTF-8") as f:
        write_date = f.write(text)
        return (write_date)
