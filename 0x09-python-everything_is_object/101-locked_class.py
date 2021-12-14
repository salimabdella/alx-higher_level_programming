#!/usr/bin/python3
"""
LockedClass
"""

class LockedClass:
    """
    class can't set attributes other than first_name
    """
    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attribute}'")
