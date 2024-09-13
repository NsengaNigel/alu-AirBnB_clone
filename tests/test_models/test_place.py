#!/usr/bin/python3
"""Unittest for Place class"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up for the tests"""
        self.place = Place()

    def test_initialization(self):
        """Test that the Place class initializes correctly"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsNotNone(self.place.id)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)

    def test_name_attr(self):
        """Test the name attribute"""
        self.place.name = "My House"
        self.assertEqual(self.place.name, "My House")

    def test_city_id_attr(self):
        """Test the city_id attribute"""
        self.place.city_id = "5678"
        self.assertEqual(self.place.city_id, "5678")

if __name__ == '__main__':
    unittest.main()
