#!/usr/bin/python3
"""File Storage Module."""
import json


class FileStorage:
    """FileStorage Class Implementation."""

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of all classes."""
        from models.base_model import BaseModel
        from models.user import User

        return {
            'BaseModel': BaseModel,
            'User': User
        }

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Update the __objects with the current object."""
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serialize __objects to JSON file to __file_path."""
        serial_objects = {}
        for key, obj in self.__objects.items():
            serial_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serial_objects, file)

    def reload(self):
        """Read and deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                load_file = json.load(file)
                for key, obj_dict in load_file.items():
                    class_name, _ = key.split('.')
                    cls = self.classes()[class_name]
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
