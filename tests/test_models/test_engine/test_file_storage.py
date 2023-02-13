import os
import tempfile
import unittest

from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_path = self.temp_file.name
        self.storage = FileStorage(self.temp_path)
        self.model = BaseModel()
        self.model.name = "test"
        self.model.number = 42
        self.storage.new(self.model)
        self.storage.save()

    def tearDown(self):
        os.remove(self.temp_path)

    def test_all(self):
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn(f"BaseModel.{self.model.id}", obj_dict)
        self.assertEqual(obj_dict[f"BaseModel.{self.model.id}"]["name"], "test")
        self.assertEqual(obj_dict[f"BaseModel.{self.model.id}"]["number"], 42)

    def test_new(self):
        model = BaseModel()
        self.storage.new(model)
        obj_dict = self.storage.all()
        self.assertIn(f"BaseModel.{model.id}", obj_dict)

    def test_save(self):
        with open(self.temp_path) as f:
            content = f.read()
        self.assertTrue(content)
        self.storage.new(BaseModel())
        self.storage.save()
        with open(self.temp_path) as f:
            content = f.read()
        self.assertTrue(content)

    def test_classes(self):
        classes = self.storage.classes()
        self.assertIsInstance(classes, dict)
        self.assertIn("BaseModel", classes)
        self.assertEqual(classes["BaseModel"], BaseModel)

    def test_reload(self):
        os.remove(self.temp_path)
        with self.assertRaises(FileNotFoundError):
            self.storage.reload()
        self.storage.new(BaseModel())
        self.storage.save()
        self.storage.reload()
        obj_dict = self.storage.all()
        self.assertIn("BaseModel." + list(obj_dict.keys())[0].split(".")[1], obj_dict)


if __name__ == '__main__':
    unittest.main()
