import unittest
import linear_search as ls
import math

class TestMethods(unittest.TestCase):
    def setUp(self):
        print("Test started.")
    def TestPassed(self):
        self.assertAlmostEqual(ls.linear_search(-(math.pi / 2), math.pi / 2), -1.57079600431)
        print("OK.")
    def tearDown(self):
        print("Test ended.")


if __name__ == "__main__":
    unittest.main()