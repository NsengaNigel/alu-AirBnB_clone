#!/usr/bin/python3
"""The class for file storage operations.

Manages serialization and deserialization of instances to/from a JSON file.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects currently stored.

        Returns:
            dict: A dictionary of all objects currently stored.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage.

        Args:
            obj (object): The object to be added to the storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists.

        Reloads the objects from the JSON file into the storage.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    # Dynamically load the class using eval
                    self.new(eval(class_name)(**value))
        except (json.JSONDecodeError, KeyError):
            pass
