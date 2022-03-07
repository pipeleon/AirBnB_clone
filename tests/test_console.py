#!/usr/bin/python3
"""Test module for the Console class"""
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Test console"""

    def test_reset(self):
        """Reset the data of FileStorage."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_setUp(self):
        """Configurate cases of test."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.test_reset()

    def test_class(self):
        """
        check if the class requereiment are or they are not
        """
        city1 = City()
        amenity1 = Amenity()
        state1 = State()
        rev1 = Review()
        place1 = Place()
        user1 = User()
        basemodel1 = BaseModel()
        self.assertEqual(city1.__class__.__name__, "City")
        self.assertEqual(amenity1.__class__.__name__, "Amenity")
        self.assertEqual(state1.__class__.__name__, "State")
        self.assertEqual(rev1.__class__.__name__, "Review")
        self.assertEqual(place1.__class__.__name__, "Place")
        self.assertEqual(user1.__class__.__name__, "User")
        self.assertEqual(basemodel1.__class__.__name__, "BaseModel")

    def test_father(self):
        """
        Check if every class inherit good
        """
        city1 = City()
        amenity1 = Amenity()
        state1 = State()
        rev1 = Review()
        place1 = Place()
        user1 = User()
        self.assertTrue(issubclass(city1.__class__, BaseModel))
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))
        self.assertTrue(issubclass(state1.__class__, BaseModel))
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
        self.assertTrue(issubclass(place1.__class__, BaseModel))
        self.assertTrue(issubclass(user1.__class__, BaseModel))


if __name__ == '__main__':
    unittest.main()
