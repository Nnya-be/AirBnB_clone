#!/usr/bin/python3
import json
from os.path import isfile


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        se_objs = {k: ob.to_dict() for k, ob in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(se_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel

        classes = {
            'BaseModel': BaseModel,
        }
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    cls_name = obj_dict['__class__']
                    cls = classes[cls_name]
                    obj = cls(**obj_dict)
                    self.all()[key] = obj
                    print(obj)
