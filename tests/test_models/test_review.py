#!/usr/bin/python3
"""Review Test Module."""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Test review class."""

    def __init__(self, *args, **kwargs):
        """Init method."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test place id."""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test for the user id."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test for the review text."""
        new = self.value()
        self.assertEqual(type(new.text), str)
