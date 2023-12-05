#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

"""Base model implementation that all models would inherit from."""


class BaseModel():
    """Base model class."""
    
    def __init__(self):
        """Initialize the class when an instance is created."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints the string format of the class."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")


    def save(self):
        """Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()


    def to_dict(self):
                """returns a dictionary containing all keys/values of __dict__ of the instance.
                """
                class_dict = dict(self.__dict__)
                class_dict['__class__'] = self.__class__.__name__
                class_dict['created_at'] = self.created_at.isoformat()
                class_dict['updated_at'] = self.updated_at.isoformat()
                return (class_dict)
