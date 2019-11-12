import unittest
import dichotomy as d
import math

class TestMethods(unittest.TestCase):
    def setUp(self):
        print("Test started.")
    def TestPassed(self):
        self.assertAlmostEqual(d.half_divide_method(-(math.pi / 2), math.pi / 2), -1.57079600431)
        print("OK.")
    def tearDown(self):
        print("Test ended.")


if __name__ == "__main__":
    unittest.main()