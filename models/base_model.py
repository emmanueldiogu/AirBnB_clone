#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:
    """Base Model Class
    Base Model Class for other model related classes to use.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise public instance attribute
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

    def __str__(self):
        """string representation

        Returns:
            str: String representation of
            [<class name>] (self.id) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Save update
        Saves the updated attribute with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary

        Returns:
            dict: returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
