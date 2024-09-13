#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def test_initialization(self):
        """Test that the Amenity class initializes correctly"""
        self.assertEqual(self.amenity.name, "")
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)

    def test_name_attr(self):
        """Test the name attribute"""
        self.amenity.name = "WiFi"
        self.assertEqual(self.amenity.name, "WiFi")

if __name__ == '__main__':
    unittest.main()
