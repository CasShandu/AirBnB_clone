#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime
import os
import json

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for BaseModel class functionalities.
    """

    def setUp(self):
        """
        Set up resources required before each test method.
        """
        pass

    def tearDown(self):
        """
        Clean up resources after each test method.
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """
        Test default initialization of BaseModel.
        """
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """
        Test initialization of BaseModel from dictionary (kwargs).
        """
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertIsNot(new, i)

    def test_kwargs_int(self):
        """
        Test initialization with non-string keys in dictionary (kwargs).
        """
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        Test save method of BaseModel.
        """
        i = BaseModel()
        i.save()
        key = "BaseModel." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Test __str__ method of BaseModel.
        """
        i = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(i.id, i.__dict__)
        self.assertEqual(str(i), expected_str)

    def test_todict(self):
        """
        Test to_dict method of BaseModel.
        """
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        with self.assertRaises(TypeError):
            new = BaseModel(**{None: None})

    def test_kwargs_one(self):
        """
        Test initialization with invalid key in kwargs.
        """
        n = {
            'id': 'some-id',
            'created_at': '2024-07-25T12:00:00.000000',
            'updated_at': '2024-07-25T12:00:00.000000',
            'Name': 'test'
        }
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_id(self):
        """
        Test id attribute type of BaseModel.
        """
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        Test created_at attribute type of BaseModel.
        """
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test updated_at attribute type and updating behavior of BaseModel.
        """
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        initial_updated_at = new.updated_at
        new.save()
        self.assertNotEqual(new.updated_at, initial_updated_at)

if __name__ == '__main__':
    unittest.main()

