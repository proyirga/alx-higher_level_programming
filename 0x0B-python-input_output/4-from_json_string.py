#!/usr/bin/python3
"""
Function that returns an obj represented by JSON
"""

import json


def from_json_string(my_str):
    """Return string rep of json"""
    return json.load(my_str)
