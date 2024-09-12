#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Base class that defines all common attributes and methods for other classes."""
    
    def __init__(self):
        """Initializes a new instance with a unique ID and timestamps."""
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.created_at = datetime.now()  # Set the current time
        self.updated_at = datetime.now()  # Set the current time

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance's __dict__."""
        dict_rep = self.__dict__.copy()  # Make a copy of the __dict__
        dict_rep["__class__"] = self.__class__.__name__  # Add the class name
        dict_rep["created_at"] = self.created_at.isoformat()  # Convert to ISO format
        dict_rep["updated_at"] = self.updated_at.isoformat()  # Convert to ISO format
        return dict_rep


