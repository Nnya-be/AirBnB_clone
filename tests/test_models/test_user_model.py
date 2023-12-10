#!/usr/bin/python3
"""Test of the user model."""
import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """Test Model for user."""

    def test_empty_values(self):
        """Test empty value."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_json_serialization(self):
        """Test for serialization of the User model."""
        user = User(email="test@example.com", password="password111")
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)

    def test_deserialization(self):
        """Test for the desirialization of the user model."""
        user_dict = {
            "email": "test@example.com",
            "password": "password111"
        }
        user = User(**user_dict)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password111")


if __name__ == "__main__":
    unittest.main()
