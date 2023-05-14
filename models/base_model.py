#!/usr/bin/python3
"""
Base Model Class for other model related classes to use.
"""

from datetime import datetime
import uuid


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """
        Initialise public instance attribute
        """
        if kwargs:
            for key, value in kwargs.items():
                if isinstance(value, datetime):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of object
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save the object with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return dictionary representation of object
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
