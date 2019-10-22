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

    def test_display_without_x_y(self):

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

    def test_str(self):

        r = Rectangle(1, 2, 3, 4, 5)
        expected = "[Rectangle] (5) 3/4 - 1/2\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_full_display(self):

        r = Rectangle(3, 2, 2, 1)

        height = 2
        width = 3
        x = 2
        y = 1
        expected = ""

        for k in range(y):
            expected += "\n"

        i = 0
        while (i < height):

            for l in range(x):
                expected += " "

            j = 0
            while(j < width):
                expected += "#"
                j += 1

            expected += "\n"
            i += 1

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):

        r = Rectangle(3, 2, 2, 1, 6)

        expected = "[Rectangle] (6) 2/1 - 3/2\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r)
            self.assertEqual(fake_out.getvalue(), expected)

        self.assertEqual(fake_out.getvalue(), expected)
