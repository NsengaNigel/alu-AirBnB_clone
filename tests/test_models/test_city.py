#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def test_initialization(self):
        """Test that the City class initializes correctly"""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.assertIsNotNone(self.city.id)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)

    def test_name_attr(self):
        """Test the name attribute"""
        self.city.name = "San Francisco"
        self.assertEqual(self.city.name, "San Francisco")

    def test_state_id_attr(self):
        """Test the state_id attribute"""
        self.city.state_id = "1234"
        self.assertEqual(self.city.state_id, "1234")

if __name__ == '__main__':
    unittest.main()
