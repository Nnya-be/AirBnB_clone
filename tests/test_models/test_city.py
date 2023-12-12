#!/usr/bin/python3
"""City Test Module."""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """TestCity class."""

    def __init__(self, *args, **kwargs):
        """Initialize with the required fileds."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the ID."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test state name."""
        new = self.value()
        self.assertEqual(type(new.name), str)
