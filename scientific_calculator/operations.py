"""Core mathematical operations for the scientific calculator."""
from __future__ import annotations

import cmath
import math
from typing import Tuple


# Basic arithmetic operations

def add(a: float, b: float) -> float:
    """Return the sum of *a* and *b*."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of *a* minus *b*."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of *a* and *b*."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return *a* divided by *b* raising ValueError on division by zero."""
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b


def modulus(a: float, b: float) -> float:
    """Return the modulus of *a* by *b*."""
    if b == 0:
        raise ValueError("Modulus by zero is undefined.")
    return a % b


def power(a: float, b: float) -> float:
    """Return *a* raised to the power of *b*."""
    return math.pow(a, b)


# Scientific operations

def square_root(value: float) -> float:
    """Return the square root of *value*; only defined for non-negative inputs."""
    if value < 0:
        raise ValueError("Square root requires a non-negative value.")
    return math.sqrt(value)


def cube_root(value: float) -> float:
    """Return the cube root of *value*, supporting negative inputs."""
    if value < 0:
        return -(-value) ** (1.0 / 3.0)
    return value ** (1.0 / 3.0)


def nth_root(value: float, n: int) -> float:
    """Return the nth root of *value* raising ValueError for invalid inputs."""
    if n == 0:
        raise ValueError("The zeroth root is undefined.")
    if value < 0:
        if n % 2 == 0:
            raise ValueError("Even roots of negative numbers are undefined in the reals.")
        return -(-value) ** (1.0 / n)
    return value ** (1.0 / n)


def factorial(n: int) -> int:
    """Return n! enforcing that *n* is a non-negative integer."""
    if not isinstance(n, int):
        raise ValueError("Factorial requires an integer input.")
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    return math.factorial(n)


def natural_log(value: float) -> float:
    """Return the natural logarithm of *value* for positive inputs."""
    if value <= 0:
        raise ValueError("Natural logarithm requires a positive value.")
    return math.log(value)


def log_base_10(value: float) -> float:
    """Return log10 of *value* for positive inputs."""
    if value <= 0:
        raise ValueError("Logarithm base 10 requires a positive value.")
    return math.log10(value)


def sine(value: float, degrees: bool = False) -> float:
    """Return sin(value); treat *value* as degrees when *degrees* is True."""
    angle = math.radians(value) if degrees else value
    return math.sin(angle)


def cosine(value: float, degrees: bool = False) -> float:
    """Return cos(value); treat *value* as degrees when *degrees* is True."""
    angle = math.radians(value) if degrees else value
    return math.cos(angle)


def tangent(value: float, degrees: bool = False) -> float:
    """Return tan(value); treat *value* as degrees when *degrees* is True."""
    angle = math.radians(value) if degrees else value
    return math.tan(angle)


def arcsine(value: float, degrees: bool = False) -> float:
    """Return asin(value); output in degrees when *degrees* is True."""
    if not -1.0 <= value <= 1.0:
        raise ValueError("Arcsine is defined for values between -1 and 1.")
    result = math.asin(value)
    return math.degrees(result) if degrees else result


def arccosine(value: float, degrees: bool = False) -> float:
    """Return acos(value); output in degrees when *degrees* is True."""
    if not -1.0 <= value <= 1.0:
        raise ValueError("Arccosine is defined for values between -1 and 1.")
    result = math.acos(value)
    return math.degrees(result) if degrees else result


def arctangent(value: float, degrees: bool = False) -> float:
    """Return atan(value); output in degrees when *degrees* is True."""
    result = math.atan(value)
    return math.degrees(result) if degrees else result


def hyperbolic_sine(value: float) -> float:
    """Return sinh(value)."""
    return math.sinh(value)


def hyperbolic_cosine(value: float) -> float:
    """Return cosh(value)."""
    return math.cosh(value)


def hyperbolic_tangent(value: float) -> float:
    """Return tanh(value)."""
    return math.tanh(value)


def inverse_hyperbolic_sine(value: float) -> float:
    """Return asinh(value)."""
    return math.asinh(value)


def inverse_hyperbolic_cosine(value: float) -> float:
    """Return acosh(value); domain requires value >= 1."""
    if value < 1:
        raise ValueError("Inverse hyperbolic cosine requires value >= 1.")
    return math.acosh(value)


def inverse_hyperbolic_tangent(value: float) -> float:
    """Return atanh(value); domain requires -1 < value < 1."""
    if not -1.0 < value < 1.0:
        raise ValueError("Inverse hyperbolic tangent requires -1 < value < 1.")
    return math.atanh(value)


def exponential(value: float) -> float:
    """Return the exponential of *value* (e^value)."""
    return math.exp(value)


def absolute_value(value: float) -> float:
    """Return the absolute value of *value*."""
    return abs(value)


# Complex number operations

def complex_add(z1: complex, z2: complex) -> complex:
    """Return the sum of two complex numbers."""
    return z1 + z2


def complex_subtract(z1: complex, z2: complex) -> complex:
    """Return the difference of two complex numbers."""
    return z1 - z2


def complex_multiply(z1: complex, z2: complex) -> complex:
    """Return the product of two complex numbers."""
    return z1 * z2


def complex_divide(z1: complex, z2: complex) -> complex:
    """Return the quotient of two complex numbers."""
    if z2 == 0:
        raise ValueError("Division by zero is undefined for complex numbers.")
    return z1 / z2


def complex_magnitude(z: complex) -> float:
    """Return the magnitude of a complex number."""
    return abs(z)


def complex_argument(z: complex) -> float:
    """Return the argument (phase angle) of a complex number in radians."""
    return math.atan2(z.imag, z.real)


def complex_conjugate(z: complex) -> complex:
    """Return the complex conjugate of *z*."""
    return z.conjugate()


# Equation solving

def solve_linear(a: float, b: float) -> float:
    """Solve ax + b = 0 returning the single solution."""
    if a == 0:
        if b == 0:
            raise ValueError("Infinite solutions exist for 0x + 0 = 0.")
        raise ValueError("No solution exists when a = 0 and b != 0.")
    return -b / a


def solve_quadratic(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """Solve ax^2 + bx + c = 0 returning a tuple with two solutions."""
    if a == 0:
        solution = solve_linear(b, c)
        return (solution, solution)
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        sqrt_disc = math.sqrt(discriminant)
    else:
        sqrt_disc = cmath.sqrt(discriminant)
    denominator = 2 * a
    root1 = (-b + sqrt_disc) / denominator
    root2 = (-b - sqrt_disc) / denominator
    return (root1, root2)
