#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """This class manages storage of objects in a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves all objects to the JSON file."""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads objects from the JSON file into storage."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value.pop('__class__')
                    cls = globals()[cls_name]
                    FileStorage.__objects[key] = cls(**value)

