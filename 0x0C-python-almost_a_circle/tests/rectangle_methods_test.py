#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class RectangleMethodsTestCase(unittest.TestCase):

    def test_area(self):
        r = Rectangle(3, 2)
        r_1 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.area(), 6)
        self.assertEqual(r_1.area(), 6)

    def test_display(self):

        r = Rectangle(3, 2)

        height = 2
        width = 3
        expected = ""

        i = 0
        while (i < height):
            j = 0
            while(j < width):
                expected += "#"
                j += 1
            expected += "\n"
            i += 1

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)
