#!/usr/bin/python3
"""Unittest module for the BaseModel Class"""
import json
import uuid
import unittest

from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

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


if __name__ == '__main__':
    unittest.main()
