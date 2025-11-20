"""Expression evaluator for the arithmetic calculator."""
from __future__ import annotations

from decimal import Decimal, getcontext
from typing import Iterable, List

# Raise precision enough to comfortably handle typical calculator use cases.
getcontext().prec = 28


class CalculationError(ValueError):
    """Raised when an expression cannot be parsed or evaluated."""


def evaluate(expression: str) -> Decimal:
    """Evaluate an arithmetic expression and return a Decimal result.

    Supports +, -, *, /, parentheses, and unary +/-. Whitespace is ignored.
    Raises CalculationError for malformed expressions and ZeroDivisionError for
    divisions by zero.
    """

    if expression is None:
        raise CalculationError("Expression cannot be None.")

    stripped = expression.strip()
    if not stripped:
        raise CalculationError("Expression cannot be empty.")

    tokens = _tokenize(stripped)
    rpn = _to_rpn(tokens)
    return _evaluate_rpn(rpn)


def _tokenize(expression: str) -> List[str]:
    tokens: List[str] = []
    length = len(expression)
    i = 0

    while i < length:
        ch = expression[i]
        if ch.isspace():
            i += 1
            continue

        if ch in "+-*/()":
            tokens.append(ch)
            i += 1
            continue

        if ch.isdigit() or ch == ".":
            start = i
            has_decimal_point = ch == "."
            i += 1
            while i < length:
                current = expression[i]
                if current.isdigit():
                    i += 1
                    continue
                if current == ".":
                    if has_decimal_point:
                        raise CalculationError("Invalid number with multiple decimal points.")
                    has_decimal_point = True
                    i += 1
                    continue
                break

            token = expression[start:i]
            if token == ".":
                raise CalculationError("Standalone decimal point is not a valid number.")
            tokens.append(token)
            continue

        raise CalculationError(f"Invalid character '{ch}' in expression.")

    return tokens


_PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "u+": 3,
    "u-": 3,
}

_RIGHT_ASSOCIATIVE = {"u+", "u-"}


def _to_rpn(tokens: Iterable[str]) -> List[str]:
    output: List[str] = []
    operators: List[str] = []
    prev_type = "operator"  # Treat the start as if an operator preceded it.

    for token in tokens:
        if _is_number(token):
            output.append(token)
            prev_type = "number"
            continue

        if token == "(":
            operators.append(token)
            prev_type = "left_paren"
            continue

        if token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            if not operators:
                raise CalculationError("Mismatched parentheses detected.")
            operators.pop()  # Discard the "(".
            prev_type = "right_paren"
            continue

        # Token is an operator at this point.
        operator = token
        if token in {"+", "-"} and prev_type in {"operator", "left_paren"}:
            # Unary operator context.
            operator = "u+" if token == "+" else "u-"
        elif prev_type in {"operator", "left_paren"}:
            raise CalculationError("Operator cannot follow another operator.")

        while operators and operators[-1] != "(":
            top = operators[-1]
            if (_PRECEDENCE[top] > _PRECEDENCE[operator]) or (
                _PRECEDENCE[top] == _PRECEDENCE[operator] and operator not in _RIGHT_ASSOCIATIVE
            ):
                output.append(operators.pop())
            else:
                break

        operators.append(operator)
        prev_type = "operator"

    if prev_type in {"operator", "left_paren"}:
        raise CalculationError("Expression cannot end with an operator.")

    while operators:
        op = operators.pop()
        if op == "(":
            raise CalculationError("Mismatched parentheses detected.")
        output.append(op)

    return output


def _evaluate_rpn(tokens: Iterable[str]) -> Decimal:
    stack: List[Decimal] = []
    for token in tokens:
        if _is_number(token):
            stack.append(_to_decimal(token))
            continue

        if token in {"+", "-", "*", "/"}:
            if len(stack) < 2:
                raise CalculationError("Insufficient operands for binary operation.")
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                stack.append(left / right)
            continue

        if token in {"u+", "u-"}:
            if not stack:
                raise CalculationError("Insufficient operand for unary operation.")
            operand = stack.pop()
            stack.append(operand if token == "u+" else -operand)
            continue

        raise CalculationError(f"Unsupported token '{token}' found during evaluation.")

    if len(stack) != 1:
        raise CalculationError("Malformed expression led to remaining operands.")

    return stack[0]


def _to_decimal(token: str) -> Decimal:
    try:
        return Decimal(token)
    except Exception as exc:  # pragma: no cover - defensive guard
        raise CalculationError(f"Invalid numeric literal '{token}'.") from exc


def _is_number(token: str) -> bool:
    if not token:
        return False
    if token[0] == ".":
        return token.count(".") == 1 and token[1:].isdigit()
    if token[0].isdigit():
        if token.count(".") == 0:
            return token.isdigit()
        if token.count(".") == 1:
            integer, fractional = token.split(".")
            return (not integer or integer.isdigit()) and fractional.isdigit()
    return False

