from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        class_dict = dict(self.__dict__)
        class_dict['__class__'] = self.__class__.__name__
        class_dict['created_at'] = self.created_at.isoformat()
        class_dict['updated_at'] = self.updated_at.isoformat()
        return class_dict
