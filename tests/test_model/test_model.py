#!/usr/bin/python3
"""
Test cases for BaseModel class
"""

import unittest
import sys
import os

# Correct path construction
current_dir = os.path.dirname(os.path.abspath(__file__))  # /tests/test_model/
project_root = os.path.dirname(os.path.dirname(current_dir))  # /AirBnB_clone/
model_dir = os.path.join(project_root, 'models')  # Changed 'model' to 'models'
sys.path.append(model_dir)

# Debug prints
print("Current working directory:", os.getcwd())
print("Current dir:", current_dir)
print("Project root:", project_root)
print("Model dir:", model_dir)
print("Updated sys.path:", sys.path)

from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(str(my_model.id), str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == "__main__":
    unittest.main()
