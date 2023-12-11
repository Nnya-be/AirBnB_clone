#!/usr/bin/python3
"""File Storage Module."""
import json


class FileStorage:
    """Class Implementations for the file storage."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            serialized_obj = {}
            serialized_obj.update(FileStorage.__objects)
            for key, value in serialized_obj.items():
                serialized_obj[key] = value.to_dict()
            json.dump(serialized_obj, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User

        cls = {
            'BaseModel': BaseModel, 'User' : User,
        }
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    self.all()[key] = cls[obj_dict['__class__']](**obj_dict)
        except FileNotFoundError:
            pass
