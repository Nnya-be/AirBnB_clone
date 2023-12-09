#!/usr/bin/python3
"""Review Module."""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review Class Implementation."""

    def __init__(self, *args, **kwargs):
        """Initialize the Review."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
