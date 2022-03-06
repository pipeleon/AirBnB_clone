#!/usr/bin/python3
"""Tests class place"""
from models.base_model import BaseModel
from models.place import Place
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models


class TestPlace(unittest.TestCase):
    """Tests class place"""

    def test_subclase(self):
        """
        Subclass BasyModel
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertFalse(hasattr(place, "update_at"))

    def test_user_id(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name(self):
        """
                Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_city_id(self):
        """
                Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_description(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_bathrooms(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_longitude(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_number_rooms(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_price_by_night(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_max_guest(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_diccionario(self):
        """
            Value return of dictionary
        """
        formato = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        diccionario = place.to_dict()
        self.assertEqual(diccionario["__class__"], "Place")
        self.assertEqual(type(diccionario["created_at"]), str)
        self.assertEqual(type(diccionario["updated_at"]), str)
        self.assertEqual(
            diccionario["created_at"],
            place.created_at.strftime(formato)
        )
        self.assertEqual(
            diccionario["updated_at"],
            place.updated_at.strftime(formato))

    def test_latitude(self):
        """
            Attribute of class
        """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_to_dict_Place(self):
        """
            to_dict whit Place and the tupe and contents
        """
        place = Place()
        diccionario = place.to_dict()
        self.assertEqual(type(diccionario), dict)
        for Atributo in place.__dict__:
            self.assertTrue(Atributo in diccionario)
            self.assertTrue("__class__" in diccionario)

    def test_instance(self):
        """Instance class place"""

        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_str(self):
        """correct return method str"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))


if __name__ == '__main__':
    unittest.main()
