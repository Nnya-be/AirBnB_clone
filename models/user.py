#!/usr/bin/python3
"""User Model."""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class Implementations."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
