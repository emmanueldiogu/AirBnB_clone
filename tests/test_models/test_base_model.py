#!/usr/bin/python3
"""Unittest module for the BaseModel Class"""
import json
import uuid
import unittest

from datetime import datetime
# from models import storage
# from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_instantiate_base_model(self):
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
