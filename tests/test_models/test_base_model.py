import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_str_method(self):
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)

    def test_to_dict_datetime_format(self):
        model_dict = self.model.to_dict()
        created_at_str = model_dict['created_at']
        updated_at_str = model_dict['updated_at']
        created_at = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(updated_at_str, '%Y-%m-%dT%H:%M:%S.%f')
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def test_dict_to_instance(self):
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)

    def test_dict_to_instance_with_custom_date_format(self):
        model_dict = self.model.to_dict()
        model_dict_str = json.dumps(model_dict)
        new_model = BaseModel(**json.loads(model_dict_str))
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)


if __name__ == '__main__':
    unittest.main()
