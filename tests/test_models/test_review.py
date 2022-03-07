#!/usr/bin/python3
"""Test class Review"""
from models.base_model import BaseModel
from models.review import Review
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models


class TestReview(unittest.TestCase):
    """Test class Review"""

    def test_subclass(self):
        """"Test class Review is subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_place_id(self):
        """Attibute of class and empty"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """Attibute of class and empty the chain"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text(self):
        """Attibute of class and empty the chain"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_str(self):
        """test that the str method has the correct output"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

    def test_to_dict_values(self):
        """values in dict returned from to_dict are correct"""
        format_date = "%Y-%m-%dT%H:%M:%S.%f"
        rev = Review()
        di = rev.to_dict()
        self.assertEqual(di["__class__"], "Review")
        self.assertEqual(type(di["created_at"]), str)
        self.assertEqual(type(di["updated_at"]), str)
        self.assertEqual(di["creat_at"], rev.created_at.strftime(format_date))
        self.assertEqual(di["updat_at"], rev.updated_at.strftime(format_date))

    def test_to_dict_creates_dict(self):
        """to_dict creates a dictionary with the appropriate attributes"""
        review = Review()
        dictionary = review.to_dict()
        self.assertEqual(type(dictionary), dict)
        for Attribut in review.__dict__:
            self.assertTrue(Attribut in dictionary)
            self.assertTrue("__class__" in dictionary)

    def test_instance(self):
        """Try instantiating the Review class"""

        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))


if __name__ == '__main__':
    unittest.main()
