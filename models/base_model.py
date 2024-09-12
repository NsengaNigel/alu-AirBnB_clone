#!/usr/bin/python3
"""BaseModel class module - defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime

class BaseModel:
    """A base class for all models, with common attributes and methods"""

    def __init__(self):
        """Initialize a new instance of BaseModel"""
        self.id = str(uuid.uuid4())  # Generate a unique id
        self.created_at = datetime.now()  # Set creation date and time
        self.updated_at = self.created_at  # Set update date and time

    def __str__(self):
        """Return string representation of the BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all instance attributes"""
        obj_dict = self.__dict__.copy()  # Copy the instance's __dict__
        obj_dict['__class__'] = self.__class__.__name__  # Add class name to the dictionary
        obj_dict['created_at'] = self.created_at.isoformat()  # Convert datetime to ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Convert datetime to ISO format
        return obj_dict

