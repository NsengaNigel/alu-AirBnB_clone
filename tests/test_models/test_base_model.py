#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import time
from io import StringIO
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance(self):
        """Test if object is an instance of BaseModel."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_class_type(self):
        """Test the class type of the instance."""
        base = BaseModel()
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """Test the save method updates the updated_at attribute."""
        base = BaseModel()
        old_time = base.updated_at
        time.sleep(1)
        base.save()
        self.assertNotEqual(base.updated_at, old_time)

    def test_save_creates_file(self):
        """Test if save creates a file.json."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_str_representation(self):
        """Test the string representation of the object."""
        base = BaseModel()
        expected_output = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(base)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_init_no_args(self):
        """Test initialization without arguments."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs."""
        bm = BaseModel(id="1234", created_at="2024-09-12T00:00:00", updated_at="2024-09-12T01:00:00", name="Test")
        self.assertEqual(bm.id, "1234")
        self.assertEqual(bm.name, "Test")
        self.assertEqual(bm.created_at, datetime.fromisoformat("2024-09-12T00:00:00"))
        self.assertEqual(bm.updated_at, datetime.fromisoformat("2024-09-12T01:00:00"))

    def test_to_dict(self):
        """Test the to_dict method."""
        bm = BaseModel()
        bm.name = "Test"
        bm.my_number = 42
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["name"], "Test")
        self.assertEqual(bm_dict["my_number"], 42)
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)

    def test_str(self):
        """Test the __str__ method."""
        bm = BaseModel()
        bm_str = str(bm)
        self.assertIn(bm.__class__.__name__, bm_str)
        self.assertIn(bm.id, bm_str)

if __name__ == "__main__":
    unittest.main()
