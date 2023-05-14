#!/usr/bin/python3
"""
Test for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_init(self):
        """
        Test case for BaseModel __init__ method
        """
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str(self):
        """
        Test case for BaseModel __str__ method
        """
        bm = BaseModel()
        bm_str = str(bm)
        self.assertIsInstance(bm_str, str)

    def test_to_dict(self):
        """
        Test case for BaseModel to_dict method
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertTrue("id" in bm_dict)
        self.assertTrue("created_at" in bm_dict)
        self.assertTrue("updated_at" in bm_dict)
        self.assertTrue("__class__" in bm_dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
