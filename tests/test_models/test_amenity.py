#!/usr/bin/python3
"""Unit test for the module Amenity"""

from os import times
import unittest
from models.amenity import Amenity
from models import storage


class Test_Amenity(unittest.TestCase):
    """Test for the class Amenity"""
    instance = Amenity()
    instance.name = 'angie2'

    data_base = storage.all()
    instance_name = 'Amenity.' + instance.id

    def test_amenityinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instance_name).to_dict()
        clase_a = "<class 'models.amenity.Amenity'>"
        times = "<class 'datetime.datime'>"

        # Data types
        self.assertEqual(str(type(self.instance)), clase_a)
        self.assertEqual(str(type(self.instance.id)), "<class 'str'>")
        self.assertEqual(str(type(self.instance.created_at)), times)
        self.assertEqual(str(type(self.instance.updated_at)), times)

        # Basic features storage
        self.assertIn(self.instance_nombre, self.data_base.keys())
        self.assertIn('created_at', features.keys())
        self.assertIn('updated_at', features.keys())
        self.assertIn('id', features.keys())
        self.assertIn('name', features.keys())

        test_dict = {"id": "a693d0ab-14d0-496b-b5db-02e4a7516d4e",
                    "created_at": "2022-03-04T15:08:52.299424",
                    "updated_at": "2022-03-04T15:08:52.300076",
                    "__class__": "Amenity",
                    "name": "angie"}
        instance2 = Amenity(**test_dict)
        self.assertIsInstance(instance2, Amenity)
        self.assertEqual(instance2.id, "a693d0ab-14d0-496b-b5db-02e4a7516d4e")
        self.assertEqual(instance2.name, "angie")

    def test_amenitysave(self):
        """Test for the method save"""
        dato_update = self.instance.updated_at
        self.instance.save()
        new_date = self.instance.updated_at
        self.assertNotEqual(dato_update, new_date)

    def test_amenitytodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instance.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instance_nombre, self.data_base.keys())

if __name__ == '__main__':
    unittest.main()
