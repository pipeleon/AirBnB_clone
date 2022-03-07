#!/usr/bin/python3
"""Test for State class"""
from models.base_model import BaseModel
from models.state import State
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models


class TestState(unittest.TestCase):
    """Test State Class"""

    def test_sub_class(self):
        """
            if state class is subclass of BaseModel
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertFalse(hasattr(state, "update_at"))

    def test_name(self):
        """
        Class attribute and if the string is empty
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dictstate_create(self):
        """
            The test to_dict method creates a dictionary
            with the right attributes
        """
        state = State()
        dictionary = state.to_dict()
        self.assertEqual(type(dictionary), dict)
        for attribut in state.__dict__:
            self.assertTrue(attribut in dictionary)
            self.assertTrue("__class__" in dictionary)

    def test_str(self):
        """test that the str method has the correct output"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

    def test_to_valores_dicci(self):
        """values in dict returned from to_dict are correct"""
        formato = "%Y-%m-%dT%H:%M:%S.%f"
        state = State()
        di = state.to_dict()
        self.assertEqual(di["__class__"], "State")
        self.assertEqual(type(di["created_at"]), str)
        self.assertEqual(type(di["updated_at"]), str)
        self.assertEqual(di["created_at"], state.created_at.strftime(formato))
        self.assertEqual(di["updated_at"], state.updated_at.strftime(formato))

    def test_instancia(self):
        """Try instantiating the State class"""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))


if __name__ == '__main__':
    unittest.main()
