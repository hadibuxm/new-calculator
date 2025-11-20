"""Core arithmetic calculator implementation."""

from __future__ import annotations

import ast
from typing import Union

Number = Union[int, float]


class CalculatorError(ValueError):
    """Raised when an expression cannot be evaluated safely."""


class ArithmeticCalculator:
    """Evaluate basic arithmetic expressions while enforcing safety rules."""

    def evaluate(self, expression: str) -> Number:
        """Evaluate an arithmetic expression with +, -, *, /, and parentheses.

        Args:
            expression: String representation of the arithmetic expression.

        Returns:
            Numerical result of the expression.

        Raises:
            CalculatorError: If the expression is invalid or unsafe to evaluate.
        """

        if not isinstance(expression, str):
            raise CalculatorError("Expression must be provided as a string.")

        expression = expression.strip()
        if not expression:
            raise CalculatorError("Expression cannot be empty.")

        try:
            parsed = ast.parse(expression, mode="eval")
        except SyntaxError as exc:  # pragma: no cover - exercised via CalculatorError
            raise CalculatorError("Invalid expression syntax.") from exc

        try:
            return self._evaluate_node(parsed.body)
        except ZeroDivisionError as exc:
            raise CalculatorError("Division by zero is not allowed.") from exc

    def _evaluate_node(self, node: ast.AST) -> Number:
        if isinstance(node, ast.BinOp):
            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)
            return self._apply_operator(node.op, left, right)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            operand = self._evaluate_node(node.operand)
            return operand if isinstance(node.op, ast.UAdd) else -operand
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise CalculatorError("Only numeric literals are allowed.")
        if isinstance(node, ast.Num):  # pragma: no cover - for Python <3.8 compatibility
            return node.n
        if isinstance(node, ast.Expression):
            return self._evaluate_node(node.body)
        if isinstance(node, ast.Call):
            raise CalculatorError("Function calls are not allowed in expressions.")
        if isinstance(node, ast.Name):
            raise CalculatorError("Variable names are not allowed in expressions.")
        if isinstance(node, ast.Expr):
            return self._evaluate_node(node.value)

        raise CalculatorError(f"Unsupported expression element: {ast.dump(node, include_attributes=False)}")

    def _apply_operator(self, operator: ast.AST, left: Number, right: Number) -> Number:
        if isinstance(operator, ast.Add):
            return left + right
        if isinstance(operator, ast.Sub):
            return left - right
        if isinstance(operator, ast.Mult):
            return left * right
        if isinstance(operator, ast.Div):
            if right == 0:
                raise ZeroDivisionError
            return left / right
        raise CalculatorError("Unsupported operator encountered.")
