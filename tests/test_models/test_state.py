#!/usr/bin/python3
"""Unittest for State class"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def test_initialization(self):
        """Test that the State class initializes correctly"""
        self.assertEqual(self.state.name, "")
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)

    def test_name_attr(self):
        """Test the name attribute"""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

if __name__ == '__main__':
    unittest.main()
