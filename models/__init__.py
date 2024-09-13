#!/usr/bin/python3

"""
The class for storage configuration
"""

# models/__init__.py
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity

storage = FileStorage()
storage.reload()