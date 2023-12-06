#!/usr/bin/python3
"""Check edge cases for the __init__ method on the dict."""


import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelInit(unittest.TestCase):
    def test_empty_kwargs(self):
        """Test types withour passing kwargs."""
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_class_in_kwargs(self):
        """Test for __class__ att being present."""
        instance = BaseModel(**{'__class__ ': 'TestClass'})
        self.assertTrue(hasattr(instance, '__class__'))
        self.assertNotEqual(getattr(instance, '__class__'), 'TestClass')
        
    def test_additional_att_in_kwargs(self):
        """Test for addding  another attribute."""
        instance = BaseModel(extra_attribute='Value')
        self.assertTrue(hasattr(instance, 'extra_attribute'))
        self.assertEqual(getattr(instance, 'extra_attribute'),'Value')

    def test_string_format_dates(self):
        """Test for the string format of the dates."""
        time_str = '2023-12-06T12:30:45.678910'
        instance = BaseModel(created_at=time_str, updated_at=time_str)
        self.assertEqual(instance.created_at.isoformat(), time_str)
        self.assertEqual(instance.updated_at.isoformat(), time_str)

    def test_invalid_datetime_string(self):
        """Test for invalid input for time."""
        invalid_time_str = 'invalid_datetime_string'
        instance = BaseModel(created_at=invalid_time_str, updated_at=invalid_time_str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_class_name_mismatch(self):
        """Test for wrong names in the class."""
        instance = BaseModel(__class__='ClassName!')
        self.assertTrue(hasattr(instance, '__class__'))

    def test_class_and_other_attributes(self):
        """Test for additional attributes in the class."""
        instance = BaseModel(extra_attribute='value')
        self.assertTrue(hasattr(instance, '__class__'))
        self.assertTrue(hasattr(instance, 'extra_attribute'))
        self.assertEqual(getattr(instance, 'extra_attribute'), 'value')

    def test_random_valued_kwargs(self):
        instance = BaseModel(random_key='random_value')
        self.assertTrue(hasattr(instance, 'random_key'))
        self.assertEqual(getattr(instance, 'random_key'), 'random_value')

    def test_large_instances(self):
        instances = [BaseModel(attribute=f'value_{i}') for i in range(1000)]
        self.assertEqual(len(instances), 1000)
