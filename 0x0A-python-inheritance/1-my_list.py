#!/usr/bin/python3
"""
Module 1-my_list
inherits from class list
and prints a sorted list
"""


class MyList(list):
    """
    inherits from list

    methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
