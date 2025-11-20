import unittest
from decimal import Decimal

from calculator import CalculationError, evaluate


class TestEvaluate(unittest.TestCase):
    def test_basic_operations(self) -> None:
        self.assertEqual(evaluate("2 + 2"), Decimal("4"))
        self.assertEqual(evaluate("5 - 3"), Decimal("2"))
        self.assertEqual(evaluate("4 * 2"), Decimal("8"))
        self.assertEqual(evaluate("8 / 2"), Decimal("4"))

    def test_operator_precedence(self) -> None:
        self.assertEqual(evaluate("2 + 3 * 4"), Decimal("14"))
        self.assertEqual(evaluate("(2 + 3) * 4"), Decimal("20"))

    def test_decimals(self) -> None:
        self.assertEqual(evaluate("0.1 + 0.2"), Decimal("0.3"))
        self.assertEqual(evaluate("1.5 * 2"), Decimal("3.0"))

    def test_unary_operations(self) -> None:
        self.assertEqual(evaluate("-5 + 3"), Decimal("-2"))
        self.assertEqual(evaluate("3 * (-2 + 5) / 3"), Decimal("3"))

    def test_error_on_division_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            evaluate("5 / 0")

    def test_invalid_expression(self) -> None:
        with self.assertRaises(CalculationError):
            evaluate("2 + * 2")
        with self.assertRaises(CalculationError):
            evaluate("2 + a")
        with self.assertRaises(CalculationError):
            evaluate("")


if __name__ == "__main__":
    unittest.main()
