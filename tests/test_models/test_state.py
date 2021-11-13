#!/usr/bin/python3
"""Unittests for State Class."""

import re
import json
import unittest
import uuid
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Unit test for State"""

    def test_basic_test(self):
        """Basic tests for State class"""
        self.assertTrue(issubclass(State, BaseModel))
        my_model = State()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual([my_model.name, my_model.my_number],
                         ["Holberton", 89])

    def test_init(self):
        """Test if created_at, updated_at and id are exist"""
        my_model = State()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "name"))

    def test_init_time(self):
        """Test if created_at, updated_at are valid"""
        then = datetime.utcnow()
        my_model = State()
        now = datetime.utcnow()
        self.assertTrue(then <= my_model.created_at <= now)
        self.assertTrue(then <= my_model.updated_at <= now)
        self.assertTrue(my_model.created_at <= my_model.updated_at)

    def test_init_id(self):
        """Test if uuid is valid"""
        my_model = State()
        my_model_1 = State()
        self.assertEqual(uuid.UUID(my_model.id).version, 4)
        self.assertFalse(my_model.id == my_model_1.id)

    def test_str_method(self):
        """Tests __str__ of State class"""
        my_model = State()
        s = "[State] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), s)

    def test_save_method(self):
        """Tests save() method of BaseClass"""
        then = datetime.utcnow()
        my_model = State()
        updated_at = my_model.updated_at
        my_model.save()
        now = datetime.utcnow()
        self.assertTrue(then <= updated_at <= my_model.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict() of State class and check types inside"""
        my_model = State()
        my_model.my_number = 777
        d = dict(my_model.__dict__)
        d['__class__'] = "State"
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        self.assertEqual(d, my_model.to_dict())

        types = [str,
                 "updated_at",
                 "created_at",
                 "__class__",
                 "id",
                 "name"]
        self.assertTrue(all(isinstance(v, types[0])
                            for k, v in d.items() if k in types[1:]))

        types = [int,
                 "my_number"]
        self.assertTrue(all(isinstance(v, types[0])
                            for k, v in d.items() if k in types[1:]))

    def test_attributes(self):
        """Test attibutes"""
        self.assertEqual(type(State.name), str)


if __name__ == '__main__':
    unittest.main()
