import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str(self):
        bm = BaseModel()
        bm_str = str(bm)
        self.assertIsInstance(bm_str, str)

    def test_save(self):
        bm = BaseModel()
        updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(updated_at, bm.updated_at)

    def test_to_dict(self):
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
