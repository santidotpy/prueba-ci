import unittest

from factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(24, factorial(4))


if __name__ == '__main__':
    unittest.main()