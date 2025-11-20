"""Unit tests for the arithmetic calculator."""

import unittest

from calculator import ArithmeticCalculator, CalculatorError


class ArithmeticCalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = ArithmeticCalculator()

    def test_addition(self) -> None:
        self.assertEqual(self.calculator.evaluate("2 + 3"), 5)

    def test_subtraction(self) -> None:
        self.assertEqual(self.calculator.evaluate("10 - 4"), 6)

    def test_multiplication(self) -> None:
        self.assertEqual(self.calculator.evaluate("3 * 7"), 21)

    def test_division(self) -> None:
        self.assertEqual(self.calculator.evaluate("8 / 4"), 2.0)

    def test_division_returns_float(self) -> None:
        self.assertEqual(self.calculator.evaluate("5 / 2"), 2.5)

    def test_order_of_operations(self) -> None:
        self.assertEqual(self.calculator.evaluate("2 + 3 * 4"), 14)

    def test_parentheses(self) -> None:
        self.assertEqual(self.calculator.evaluate("(2 + 3) * 4"), 20)

    def test_decimal_numbers(self) -> None:
        self.assertEqual(self.calculator.evaluate("5.5 + 4.5"), 10.0)

    def test_unary_operators(self) -> None:
        self.assertEqual(self.calculator.evaluate("-5 + 3"), -2)

    def test_division_by_zero(self) -> None:
        with self.assertRaisesRegex(CalculatorError, "Division by zero is not allowed."):
            self.calculator.evaluate("10 / 0")

    def test_rejects_invalid_characters(self) -> None:
        with self.assertRaises(CalculatorError):
            self.calculator.evaluate("__import__('os').system('rm -rf /')")

    def test_rejects_empty_input(self) -> None:
        with self.assertRaisesRegex(CalculatorError, "Expression cannot be empty."):
            self.calculator.evaluate("   ")

    def test_rejects_non_string_input(self) -> None:
        with self.assertRaisesRegex(CalculatorError, "Expression must be provided as a string."):
            self.calculator.evaluate(123)  # type: ignore[arg-type]

    def test_nested_parentheses(self) -> None:
        self.assertAlmostEqual(self.calculator.evaluate("((1 + 2) * (3 + 4)) / 5"), 4.2)


if __name__ == "__main__":
    unittest.main()
