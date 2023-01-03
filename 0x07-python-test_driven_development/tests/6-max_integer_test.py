#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

  def test_max(self):
        """Test a list"""
        res = max_integer([1, 2, 4, 3])
        self.assertEqual(res, 4)
  
  def test_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
