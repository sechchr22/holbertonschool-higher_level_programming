#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_no_arguments(self):

        pt1 = "__init__() missing 2 required positional "
        pt2 = "arguments: 'width' and 'height'"
        msg = pt1 + pt2

        with self.assertRaises(TypeError) as error:
            obj = Rectangle()

        self.assertTrue(msg in str(error.exception))

    def test_one_argument(self):

        msg = "__init__() missing 1 required positional argument: 'height'"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1)

        self.assertTrue(msg in str(error.exception))

    def test_id_None(self):

        obj = Rectangle(1, 2)
        self.assertEqual(obj.id, 1)

    def test_all_arguments(self):

        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)
        self.assertEqual(obj.id, 5)

    def test_width_inf(self):

        inf = float('inf')

        msg = "width must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(inf, 2, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_width_nan(self):

        nan = float('nan')

        msg = "width must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(nan, 2, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_width_not_int(self):

        msg = "width must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle('a', 2, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_width_zero(self):

        msg = "width must be > 0"

        with self.assertRaises(ValueError) as error:
            obj = Rectangle(0, 2, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_width_negative(self):

        msg = "width must be > 0"

        with self.assertRaises(ValueError) as error:
            obj = Rectangle(-1, 2, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_height_inf(self):

        inf = float('inf')

        msg = "height must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, inf, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_height_nan(self):

        nan = float('nan')

        msg = "height must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, nan, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_height_not_int(self):

        msg = "height must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, 'a', 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_height_zero(self):

        msg = "height must be > 0"

        with self.assertRaises(ValueError) as error:
            obj = Rectangle(1, 0, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_height_negative(self):

        msg = "height must be > 0"
        with self.assertRaises(ValueError) as error:
            obj = Rectangle(1, -2, 3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_x_inf(self):

        inf = float('inf')

        msg = "x must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, 2, inf, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_x_nan(self):

        nan = float('nan')

        msg = "x must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, 2, nan, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_x_not_int(self):

        msg = "x must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, 2, 'a', 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_x_negative(self):

        msg = "x must be >= 0"

        with self.assertRaises(ValueError) as error:
            obj = Rectangle(1, 2, -3, 4, 5)

        self.assertTrue(msg in str(error.exception))

    def test_y_inf(self):

        inf = float('inf')

        msg = "y must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, 2, 3, inf, 5)

        self.assertTrue(msg in str(error.exception))

    def test_y_nan(self):

        nan = float('nan')

        msg = "y must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, 2, 3, nan, 5)

        self.assertTrue(msg in str(error.exception))

    def test_y_not_int(self):

        msg = "y must be an integer"

        with self.assertRaises(TypeError) as error:
            obj = Rectangle(1, 2, 3, 'a', 5)

        self.assertTrue(msg in str(error.exception))

    def test_y_negative(self):

        msg = "y must be >= 0"

        with self.assertRaises(ValueError) as error:
            obj = Rectangle(1, 2, 3, -4, 5)
        self.assertTrue(msg in str(error.exception))

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
