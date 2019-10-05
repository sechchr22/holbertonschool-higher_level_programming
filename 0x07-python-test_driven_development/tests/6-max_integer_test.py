#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 5, 16, 42]), 42)
        self.assertEqual(max_integer([1, 5, 16, 40 + 2]), 42)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([2, 2, 2, 2, 4]), 4)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-5, -10, -1]), -1)
        self.assertEqual(max_integer([0, 1, -1]), 1)
