#!/usr/bin/python3
"""Module for managing file storage for models."""

import json
from models.base_model import BaseModel

class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for key, value in objs.items():
                cls_name = value['__class__']
                if cls_name in globals():
                    cls = globals()[cls_name]
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

 
