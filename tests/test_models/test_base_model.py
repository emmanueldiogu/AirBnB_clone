#!/usr/bin/python3
"""Unittest module for the BaseModel Class"""
import json
import os
import uuid
import unittest

from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        self.model = BaseModel('test_model')

    def test_get_name(self):
        self.assertEqual(self.model.get_name(), 'test_model')

    def test_set_name(self):
        self.model.set_name('new_name')
        self.assertEqual(self.model.get_name(), 'new_name')

    def test_instantce_of_base_model(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updated_at(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_convert_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"],
                         model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         model.updated_at.isoformat())
        self.assertEqual(len(model_dict.keys()), 4)

    def test_str_representation_of_base_model(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIsInstance(model_str, str)
        self.assertEqual(model_str, "[BaseModel] ({}) {}".format(
            model.id, model.__dict__))

    def test_delete(self):
        self.model.save()
        self.model.delete()
        self.assertFalse(self.model.get_name() in BaseModel.get_all_names())

    def test_base_model_attributes(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_base_model_id(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_base_model_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_base_model_updated_at(self):
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_base_model_str(self):
        model = BaseModel()
        self.assertIn("[BaseModel]", str(model))
        self.assertIn("'id': '{}',".format(model.id), str(model))

    def test_base_model_save(self):
        model = BaseModel()
        updated_at = model.updated_at
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_base_model_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_base_model_init_dict(self):
        model_dict = {
            "id": "123",
            "created_at": "2022-01-01T00:00:00.000000",
            "updated_at": "2022-01-01T00:00:00.000000",
            "name": "John",
            "__class__": "BaseModel"
        }
        model = BaseModel(**model_dict)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.name, "John")
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
