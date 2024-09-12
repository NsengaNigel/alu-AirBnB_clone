#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """Class to handle file storage of model instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to a JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        cls = BaseModel
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
 
