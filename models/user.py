#!/usr/bin/python3

"""
The User model
"""

from models.base_model import BaseModel

class User:
    """"
    Attributes for the user model
    """
    email = ""                  # email: string
    password = ""               # password: string
    first_name = ""             # first_name: string
    last_name = ""              # last_name: string

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super().__init__(*args, **kwargs) # A call the the super constructor