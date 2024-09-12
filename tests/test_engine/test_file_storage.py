#!/usr/bin/python3
"""Unit tests for the FileStorage class."""

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.storage = FileStorage()
        cls.storage.reload()  # Ensure we start with a fresh state

    def setUp(self):
        """Set up for individual test cases."""
        self.storage.all().clear()

    def test_all(self):
        """Test the all() method."""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIn(f"BaseModel.{bm.id}", all_objs)

    def test_new(self):
        """Test the new() method."""
        bm = BaseModel()
        self.storage.new(bm)
        all_objs = self.storage.all()
        self.assertIn(f"BaseModel.{bm.id}", all_objs)

    def test_save(self):
        """Test the save() method."""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            content = json.load(f)
        self.assertIn(f"BaseModel.{bm.id}", content)

    def test_reload(self):
        """Test the reload() method."""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.storage.all().clear()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(f"BaseModel.{bm.id}", all_objs)

if __name__ == '__main__':
    unittest.main()

