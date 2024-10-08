#!/usr/bin/python3
"""
BaseModel module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class that defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        from models import storage  # Import here to avoid circular import
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute `updated_at`
        with the current datetime.
        """

        from models import storage  # Import here to avoid circular import
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of the instance's __dict__.
        Adds __class__ key with the class name.
        Converts created_at and updated_at to ISO
        format strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
