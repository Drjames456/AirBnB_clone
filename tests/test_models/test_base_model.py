#!/usr/bin/python3
"""A module to test the base class and the methods in it"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A class to for the base model to test the methods"""
    def test_init(self):
        """A test for the constructor of the base class"""
        div1 = BaseModel()
        div2 = BaseModel()
        self.assertIsInstance(div1, BaseModel)
        self.assertNotEqual(div1, div2)

    def test_uuid(self):
        """A test for the uuid of different instance"""
        giv1 = BaseModel()
        giv2 = BaseModel()
        self.assertNotEqual(giv1.id, giv2.id)
        self.assertIsInstance(giv1.id, str)
