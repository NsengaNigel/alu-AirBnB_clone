#!/usr/bin/python3

"""
The class for file storage operations
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Returns the dictionary of all objects currently stored.

    Returns:
        dict: A dictionary of all objects currently stored.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Prints all string representation of all instances based or not on the class name. 

        Usage:
            all <class name>
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (object): The object to be added to the storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Save the objects to the json file
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)


    def reload(self):
        """
        Reloads the objects from the JSON file into the storage.
        """

        if not os.path.isfile(FileStorage.__file_path):
            return
        
        with open(FileStorage.__file_path, 'r') as file:
            try:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.new(eval(class_name)(**value))
            except json.JSONDecodeError:
                pass