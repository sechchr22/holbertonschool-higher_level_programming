#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    """Unittest for Base"""

    def test_id_is_none(self):
        """if id is None"""
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_id_is_not_none(self):
        """if id is not None"""
        obj = Base(22)
        self.assertEqual(obj.id, 22)

    def test_inf(self):
        """if index inf"""
        inf = float('inf')
        obj = Base(inf)
        self.assertEqual(obj.id, inf)

    def test_negative(self):
        """if negative index"""
        obj = Base(-1)
        self.assertEqual(obj.id, -1)

if __name__ == '__main__':
    unittest.main()
