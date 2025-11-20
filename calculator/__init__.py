"""Arithmetic calculator package exposing the main evaluate API."""
from .evaluator import CalculationError, evaluate

__all__ = ["evaluate", "CalculationError"]
