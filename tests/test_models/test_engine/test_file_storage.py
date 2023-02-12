#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_file_storage_attributes(self):
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))

    def test_file_storage_all(self):
        storage = FileStorage()
        model1 = BaseModel()
        model2 = BaseModel()
        storage.new(model1)
        storage.new(model2)
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn("{}.{}".format(
            type(model1).__name__, model1.id), objects.keys())
        self.assertIn("{}.{}".format(
            type(model2).__name__, model2.id), objects.keys())

    def test_file_storage_new(self):
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        self.assertIn("{}.{}".format(type(model).__name__, model.id),
                      storage._FileStorage__objects.keys())

    def test_file_storage_save(self):
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        with open(storage._FileStorage__file_path, "r") as f:
            file_contents = f.read()
        self.assertIn("{}.{}".format(
            type(model).__name__, model.id), file_contents)

    def test_file_storage_reload(self):
        storage1 = FileStorage()
        model1 = BaseModel()
        storage1.new(model1)
        storage1.save()

        storage2 = FileStorage()
        self.assertNotIn("{}.{}".format(type(model1).__name__,
                         model1.id), storage2.all().keys())
        storage2.reload()


if __name__ == '__main__':
    unittest.main()
