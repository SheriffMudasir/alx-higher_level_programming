#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
        def test_max_integer(self):

                """Test for max number"""
                self.assertEqual(max_integer([25, 6, 7, 5]), 25)

        def test_string_in_list(self):
                """Test when string in list"""
                with self.assertRaises(TypeError):
                        max_integer([2, 5, "School"])

        def test_negative(self):
                """Test when negative number is in the list"""
                self.assertEqual(max_integer([-4, 4, 3]), 4)



if __name__ == "__main__":
        unittest.main()
