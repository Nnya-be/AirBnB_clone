#!/usr/bin/python3
"""Amenity Module."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class implementation."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
