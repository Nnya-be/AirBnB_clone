#!/usr/bin/python3
"""Base model implementation that all models would inherit from."""
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Base model class."""

    def __init__(self):
        """Initialize the class when an instance is created."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """Print the string format of the class."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update the updated_at with the current datetime."""
        if hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()
        else:
            raise AttributeError("Object not fully initialized.")
            
    def to_dict(self):
        """Return a dictionary containing all keys/values on the instance."""
        class_dict = dict(self.__dict__)
        class_dict['__class__'] = self.__class__.__name__
        class_dict['created_at'] = self.created_at.isoformat()
        class_dict['updated_at'] = self.updated_at.isoformat()
        return (class_dict)
