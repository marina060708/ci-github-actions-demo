# test_main.py
import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 7), 7)

    def test_add_negative(self):
        self.assertEqual(add(-2, 3), 1)

if __name__ == "__main__":
    unittest.main()
