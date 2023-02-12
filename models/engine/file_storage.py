#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    # def reload(self):
    #     try:
    #         with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
    #             obj_dict = json.load(f)
    #         for key, value in obj_dict.items():
    #             class_name = value['__class__']
    #             del value['__class__']
    #             FileStorage.__objects[key] = eval(class_name)(**value)
    #     except FileNotFoundError:
    #         pass
    
    def reload(self):
        """Deserializes the JSON file to create BaseModel objects."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value['__class__']
                del value['__class__']
                cls = self.classes()[class_name]
                instance = cls(**value)
                FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
