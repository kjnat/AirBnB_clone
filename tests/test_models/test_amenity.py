#!/usr/bin/python3
"""Unittests for Amenity Class."""

import re
import json
import unittest
import uuid
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity_8(unittest.TestCase):

    """Unit test for Amenity"""

    def test_basic_test(self):
        """Basic tests for Amenity class"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        my_model = Amenity()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual([my_model.name, my_model.my_number],
                         ["Holberton", 89])

    def test_init(self):
        """Test if created_at, updated_at and id are exist"""
        my_model = Amenity()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "name"))

    def test_init_time(self):
        """Test if created_at, updated_at are valid"""
        then = datetime.utcnow()
        my_model = Amenity()
        now = datetime.utcnow()
        self.assertTrue(then <= my_model.created_at <= now)
        self.assertTrue(then <= my_model.updated_at <= now)
        self.assertTrue(my_model.created_at <= my_model.updated_at)

    def test_init_id(self):
        """Test if uuid is valid"""
        my_model = Amenity()
        my_model_1 = Amenity()
        self.assertEqual(uuid.UUID(my_model.id).version, 4)
        self.assertFalse(my_model.id == my_model_1.id)

    def test_str_method(self):
        """Tests __str__ of Amenity class"""
        my_model = Amenity()
        s = "[Amenity] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), s)

    def test_save_method(self):
        """Tests save() method of Amenity class"""
        then = datetime.utcnow()
        my_model = Amenity()
        updated_at = my_model.updated_at
        my_model.save()
        now = datetime.utcnow()
        self.assertTrue(then <= updated_at <= my_model.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict() of Amenity class and check types inside"""
        my_model = Amenity()
        my_model.my_number = 777
        d = dict(my_model.__dict__)
        d['__class__'] = "Amenity"
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

    def test_attributes(self):
        """Test attibutes"""
        self.assertEqual(type(Amenity.name), str)


if __name__ == '__main__':
    unittest.main()
