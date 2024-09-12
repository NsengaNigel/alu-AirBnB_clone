#!/usr/bin/python3

"""
The User model
"""

from models.base_model import BaseModel

class User(BaseModel):
    """"
    User model and it's class attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, *args, **kwargs):
    #     """
    #     Constructor
    #     """
    #     super().__init__(*args, **kwargs) # A call the the super constructor