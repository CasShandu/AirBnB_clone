#!/usr/bin/python3

import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.test_file = "test_file.json"

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_FileStorage_instantiation_no_args(self):
        """Test instantiation with no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        """Test instantiation with arguments."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        """Test if storage initializes correctly."""
        self.assertEqual(type(models.storage), FileStorage)

    def test_all_storage_returns_dictionary(self):
        """Test if storage.all() returns a dictionary."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test if new objects are added to storage."""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        """Test if passing extra arguments raises TypeError."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """Test if passing None raises AttributeError."""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """Test if save and reload methods work correctly."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save_to_file(self):
        """Test if save method creates the file."""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """Test if reload handles an empty file correctly."""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__ == '__main__':
    unittest.main()

