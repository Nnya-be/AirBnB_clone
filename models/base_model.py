#!/usr/bin/python3
from datetime import datetime
import uuid
"""Base Model."""


class BaseModel:
    """Base Class and its attributes and methods."""

    def __init__(self, *args, **kwargs):
        """Initialize the class."""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        try:
                            date_format = '%Y-%m-%dT%H:%M:%S.%f'
                            setattr(self, k, datetime.strptime(v, date_format))
                        except ValueError:
                            setattr(self, k, datetime.now())
                    else:
                        setattr(self, k, v)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the string form of the class."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save a new instance."""
        from models import storage
        if hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()
        else:
            raise AttributeError("Object not fully initialized.")
            
    def to_dict(self):
        """Return a dict to the instance."""
        class_dict = dict(self.__dict__)
        class_dict['__class__'] = self.__class__.__name__
        class_dict['created_at'] = self.created_at.isoformat()
        class_dict['updated_at'] = self.updated_at.isoformat()
        return class_dict
