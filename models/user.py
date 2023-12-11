#!/usr/bin/python3
"""User Module."""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class that inherits from BaseModel."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initialization of User Instance."""
        super().__init__(*args, **kwargs)
