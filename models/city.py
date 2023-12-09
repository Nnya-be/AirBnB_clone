#!/usr/bin/python3
"""City Module."""

from models.base_model import BaseModel

class City(BaseMoel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
