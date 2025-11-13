"""Unit tests for the scientific calculator operations module."""
from __future__ import annotations

import math
import unittest

from scientific_calculator import operations as ops


class BasicOperationTests(unittest.TestCase):
    def test_addition(self) -> None:
        self.assertEqual(ops.add(2, 3), 5)

    def test_multiplication(self) -> None:
        self.assertAlmostEqual(ops.multiply(2.5, 4), 10.0)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ValueError):
            ops.divide(10, 0)


class ScientificOperationTests(unittest.TestCase):
    def test_square_root(self) -> None:
        self.assertEqual(ops.square_root(9), 3.0)

    def test_cube_root_negative(self) -> None:
        self.assertAlmostEqual(ops.cube_root(-8), -2.0)

    def test_nth_root_even_negative_raises(self) -> None:
        with self.assertRaises(ValueError):
            ops.nth_root(-16, 2)

    def test_factorial(self) -> None:
        self.assertEqual(ops.factorial(5), 120)

    def test_factorial_negative_raises(self) -> None:
        with self.assertRaises(ValueError):
            ops.factorial(-1)

    def test_natural_log_requires_positive(self) -> None:
        with self.assertRaises(ValueError):
            ops.natural_log(0)

    def test_sine_degrees(self) -> None:
        self.assertAlmostEqual(ops.sine(30, degrees=True), 0.5, places=6)

    def test_arcsine_degrees(self) -> None:
        self.assertAlmostEqual(ops.arcsine(0.5, degrees=True), 30.0, places=6)

    def test_inverse_hyperbolic_domain(self) -> None:
        with self.assertRaises(ValueError):
            ops.inverse_hyperbolic_cosine(0.5)

    def test_exponential(self) -> None:
        self.assertAlmostEqual(ops.exponential(2), math.e ** 2)


class ComplexOperationTests(unittest.TestCase):
    def test_complex_add(self) -> None:
        self.assertEqual(ops.complex_add(3 + 4j, 1 - 2j), 4 + 2j)

    def test_complex_division_by_zero(self) -> None:
        with self.assertRaises(ValueError):
            ops.complex_divide(1 + 2j, 0)

    def test_complex_argument(self) -> None:
        value = ops.complex_argument(1 + 1j)
        self.assertAlmostEqual(value, math.pi / 4, places=6)


class EquationSolverTests(unittest.TestCase):
    def test_linear_solution(self) -> None:
        self.assertEqual(ops.solve_linear(2, -4), 2)

    def test_linear_no_solution(self) -> None:
        with self.assertRaises(ValueError):
            ops.solve_linear(0, 3)

    def test_quadratic_positive_discriminant(self) -> None:
        roots = ops.solve_quadratic(1, -3, 2)
        self.assertIn(2, roots)
        self.assertIn(1, roots)

    def test_quadratic_complex_roots(self) -> None:
        roots = ops.solve_quadratic(1, 2, 5)
        self.assertEqual(len(roots), 2)
        for root in roots:
            self.assertIsInstance(root, complex)


if __name__ == "__main__":
    unittest.main()
