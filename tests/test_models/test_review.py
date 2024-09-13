#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up for the tests"""
        self.review = Review()

    def test_initialization(self):
        """Test that the Review class initializes correctly"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertIsNotNone(self.review.id)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)

    def test_text_attr(self):
        """Test the text attribute"""
        self.review.text = "Great place!"
        self.assertEqual(self.review.text, "Great place!")

    def test_place_id_attr(self):
        """Test the place_id attribute"""
        self.review.place_id = "91011"
        self.assertEqual(self.review.place_id, "91011")

if __name__ == '__main__':
    unittest.main()
