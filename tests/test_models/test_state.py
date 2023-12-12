#!/usr/bin/python3
"""Test State Module."""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Test state class."""

    def __init__(self, *args, **kwargs):
        """Initialize the class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Test the state name."""
        new = self.value()
        self.assertEqual(type(new.name), str)
