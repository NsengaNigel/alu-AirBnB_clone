#!/usr/bin/python3

"""
The class for file storage operations
"""

import json

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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Save the objects to the json file
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file, indent=2)
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Reloads the objects from the JSON file into the storage.
        """

        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    self.__objects[key] = eval(
                        f"{value['__class__']}(**{value})")
        except FileNotFoundError:
            pass