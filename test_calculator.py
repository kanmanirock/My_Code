import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = subtract(8, 3)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = multiply(4, 6)
        self.assertEqual(result, 24)

    def test_division(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

        # Test division by zero
        with self.assertRaises(ValueError):
            divide(8, 0)

if __name__ == '__main__':
    unittest.main()