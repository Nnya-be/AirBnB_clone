#!/usr/bin/python3
"""Test for Amenity"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Test class for amenity."""

    def __init__(self, *args, **kwargs):
        """Initialse test with the base model."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
