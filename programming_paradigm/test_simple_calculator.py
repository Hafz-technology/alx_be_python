import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    test
    """
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """ test addition"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """ test subtract"""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-6, -2), -4)

    def test_multiplication(self):
        """ test multiply"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_division(self):
        """ test divide"""
        self.assertEqual(self.calc.divide(12, 3), 4)
        self.assertEqual(self.calc.divide(8, 0), None)


if __name__ == "__main__":
    unittest.main()
