#!/usr/bin/python3
"""State Module."""

from models.base_model import BaseModel

class State(BaseModel):
    """State implementation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
