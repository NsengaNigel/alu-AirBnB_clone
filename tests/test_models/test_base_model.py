#!/usr/bin/python3
"""Unit tests for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up a new BaseModel instance for testing"""
        self.model = BaseModel()

    def test_id_is_unique(self):
        """Test if each BaseModel instance has a unique id"""
        another_model = BaseModel()
        self.assertNotEqual(self.model.id, another_model.id)
    
    def test_id_is_string(self):
        """Test if the id attribute is a string"""
        self.assertIsInstance(self.model.id, str)
    
    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)
    
    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)
    
    def test_save_updates_updated_at(self):
        """Test if the save method updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
    
    def test_to_dict(self):
        """Test if to_dict returns the correct dictionary representation"""
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

