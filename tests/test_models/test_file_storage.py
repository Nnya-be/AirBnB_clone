#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for testing."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        """Test all method with an empty storage."""
        result = self.storage.all()
        self.assertNotEqual(result, {})

    def test_all_not_empty(self):
        """Test all method with non-empty storage."""
        obj = BaseModel()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.storage.new(obj)
        result = self.storage.all()
        self.assertEqual(result[key].id, obj.id)
        self.assertEqual(result[key].created_at, obj.created_at)
        self.assertEqual(result[key].updated_at, obj.updated_at)

    def test_new(self):
        """Test new method."""
        obj = BaseModel()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.storage.new(obj)
        result = self.storage.all()
        self.assertEqual(result[key].id, obj.id)
        self.assertEqual(result[key].created_at, obj.created_at)
        self.assertEqual(result[key].updated_at, obj.updated_at)

    def test_save(self):
        """Test save method."""
        obj = BaseModel()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.storage.new(obj)
        self.storage.save()
        with open("file.json", 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn(key, content)

    def test_reload(self):
        """Test reload method."""
        obj = BaseModel()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        result = new_storage.all()
        self.assertEqual(result[key].id, obj.id)
        self.assertEqual(result[key].created_at, obj.created_at)
        self.assertEqual(result[key].updated_at, obj.updated_at)


if __name__ == "__main__":
    unittest.main()
