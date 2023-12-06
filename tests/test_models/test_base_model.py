#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime, timedelta
import time

class TestBaseModel(unittest.TestCase):
    """TestBaseModel for the edge cases for the BaseModel."""

    
    def test_unique_id_generation(self):
        """Test for uniqueness of 2 generated instance id's."""
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_initialized_timestamp(self):
        """Test for the time being a datetime type."""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_update_time_on_save(self):
        """Test for the difference between the updated times when we call save."""
        instance = BaseModel()
        initial_update_time = instance.updated_at
        time.sleep(1)
        instance.save()
        self.assertNotEqual(initial_update_time, instance.updated_at)

    def test_to_dict_method(self):
        """Test to_dict to see everything is returned."""
        instance = BaseModel()
        obj_dict = instance.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str_method(self):
        """Test str method for correct output."""
        instance = BaseModel()
        str_rep = str(instance)
        self.assertIn('BaseModel', str_rep)
        self.assertIn(instance.id, str_rep)

    def test_manipulating_timestamps(self):
        """Test for similarity even when we assing the time by ourselves."""
        instance = BaseModel()
        time.sleep(0.1)
        modified_time = datetime(2023, 12, 6)
        instance.created_at = modified_time
        instance.updated_at = modified_time
        self.assertEqual(instance.created_at, modified_time)
        self.assertEqual(instance.updated_at, modified_time)

    def test_save_before_initialization(self):
        """Test for incomplete initializations."""
        instance = BaseModel()
        instance.__dict__ = {}
        with self.assertRaises(AttributeError):
            instance.save()

    def test_large_number_of_instances(self):
        instances = [BaseModel() for _ in range(1000)]
        unique_ids = set(instance.id for instance in instances)
        self.assertEqual(len(unique_ids) , len(instances))

if __name__ == '__main__':
    unittest.main()
