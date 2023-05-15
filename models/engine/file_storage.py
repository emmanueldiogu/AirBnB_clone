#!/usr/bin/python3
"""
File storage module to serialize and deserialize JSON objects.
"""

import json
import os


class FileStorage:
    """
    File storage class
    """

    def __init__(self, file_path: str = "file.json"):
        """
        Initialize new FileStorage object.

        Args:
            file_path (str): Path to JSON file.
        """
        self._file_path = file_path
        self._objects = {}

    def all(self) -> dict:
        """
        Return dictionary of objects.

        Returns:
            dict: Dictionary of objects.
        """
        return self._objects

    def new(self, obj) -> None:
        """
        Set a new object in the dictionary.

        Args:
            obj (BaseModel): Object to set.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self._objects[key] = obj

    def save(self) -> None:
        """
        Serialize the objects to a JSON file.
        """
        new_dict = {}
        for key, value in self._objects.items():
            new_dict[key] = value.to_dict()
        with open(self._file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def classes(self) -> dict:
        """
        Return a dictionary of classes.

        Returns:
            dict: Dictionary of classes.
        """
        from models.base_model import BaseModel
        return {"BaseModel": BaseModel}

    def reload(self) -> None:
        """
        Deserialize the JSON file to create BaseModel objects.
        """
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
