#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):

    def test_id_is_none(self):

        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_id_is_not_none(self):

        obj = Base(22)
        self.assertEqual(obj.id, 22)

    def test_inf(self):

        inf = float('inf')
        obj = Base(inf)
        self.assertEqual(obj.id, inf)

    def test_nan(self):

        nan = float('nan')
        obj = Base(nan)
        self.assertEqual(obj.id, nan)

    def test_negative(self):

        obj = Base(-1)
        self.assertEqual(obj.id, -1)
