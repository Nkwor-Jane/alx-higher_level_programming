#!/usr/bin/python3

"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
        """Testcases for max_integer function"""

        def test_accurate(self):
            """Correct usecases"""
            self.assertEqual(max_integer([1,2,3,4]), 4)
            self.assertEqual(max_integer([]),None)
            self.assertEqual(max_integer([50, 200, 250]), 250)
            self.assertEqual(max_integer([3, -3, -100]), 3)

        def test_empty(self):
            """Test no argument is passed"""
            self.assertIsNone(max_integer())
        
        def test_incorrect(self):
            """Test for incorrect argument"""
            self.assertRaises(Exception, max_integer, ["School", 5, 6, 5])

if __name__ == '__main__':
    unittest.main()
