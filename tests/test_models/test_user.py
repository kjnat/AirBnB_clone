#!/usr/bin/python3
"""Unittests for User Class."""

import re
import json
import unittest
import uuid
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser_8(unittest.TestCase):

    """Unit test for User"""

    def test_basic_test(self):
        """Basic tests for User class"""
        my_model = User()
        self.assertTrue(issubclass(User, BaseModel))
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual([my_model.name, my_model.my_number],
                         ["Holberton", 89])

    def test_init(self):
        """Test if created_at, updated_at and id are exist"""
        my_model = User()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "email"))
        self.assertTrue(hasattr(my_model, "password"))
        self.assertTrue(hasattr(my_model, "first_name"))
        self.assertTrue(hasattr(my_model, "last_name"))

    def test_init_time(self):
        """Test if created_at, updated_at are valid"""
        then = datetime.utcnow()
        my_model = User()
        now = datetime.utcnow()
        self.assertTrue(then <= my_model.created_at <= now)
        self.assertTrue(then <= my_model.updated_at <= now)
        self.assertTrue(my_model.created_at <= my_model.updated_at)

    def test_init_id(self):
        """Test if uuid is valid"""
        my_model = User()
        my_model_1 = User()
        self.assertEqual(uuid.UUID(my_model.id).version, 4)
        self.assertFalse(my_model.id == my_model_1.id)

    def test_str_method(self):
        """Tests __str__ of User class"""
        my_model = User()
        s = "[User] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), s)

    def test_save_method(self):
        """Tests save() method of User class"""
        then = datetime.utcnow()
        my_model = User()
        updated_at = my_model.updated_at
        my_model.save()
        self.assertTrue(then <= updated_at <= my_model.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict() of User class and check types inside"""
        my_model = User()
        my_model.my_number = 777
        d = dict(my_model.__dict__)
        d['__class__'] = "User"
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        self.assertEqual(d, my_model.to_dict())

        types = [str,
                 "updated_at",
                 "created_at",
                 "__class__",
                 "id"]
        self.assertTrue(all(isinstance(v, types[0])
                            for k, v in d.items() if k in types[1:]))

        types = [int,
                 "my_number"]
        self.assertTrue(all(isinstance(v, types[0])
                            for k, v in d.items() if k in types[1:]))

    def test_attributes_email(self):
        """Test attibutes"""
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)


if __name__ == "__main__":
    unittest.main()
