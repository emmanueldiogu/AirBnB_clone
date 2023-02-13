#!/usr/bin/python3
import json
import os


class FileStorage:
    def __init__(self, file_path: str = "file.json"):
        self._file_path = file_path
        self._objects = {}

    def all(self) -> dict:
        """Returns the dictionary of objects."""
        return self._objects

    def new(self, obj) -> None:
        """Sets a new object in the dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self._objects[key] = obj

    def save(self) -> None:
        """Serializes the objects to a JSON file."""
        new_dict = {}
        for key, value in self._objects.items():
            new_dict[key] = value.to_dict()
        with open(self._file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def classes(self) -> dict:
        """Returns a dictionary of classes."""
        from models.base_model import BaseModel
        return {"BaseModel": BaseModel}

    def reload(self) -> None:
        """Deserializes the JSON file to create BaseModel objects."""
        try:
            with open(self._file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                cls = self.classes()[class_name]
                instance = cls(**value)
                self._objects[key] = instance
        except FileNotFoundError:
            pass
