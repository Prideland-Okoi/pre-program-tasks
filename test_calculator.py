import unittest
from calculator import add, subtract, multiply, divide, square


class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        result = subtract(8, 3)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = multiply(2, 5)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        result = divide(5, 0)
        self.assertEqual(result, "Cannot divide by zero")

    def test_square(self):
        result = square(4)
        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()
