#!/usr/bin/python3
"""Unit tests for BaseModel"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""
    
    def setUp(self):
        """Set up for each test"""
        self.model = BaseModel()
    
    def test_instance(self):
        """Test if the object is an instance of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)
    
    def test_id(self):
        """Test if id is a string"""
        self.assertIsInstance(self.model.id, str)

if __name__ == '__main__':
    unittest.main()
