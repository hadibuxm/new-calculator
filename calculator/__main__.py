"""Command line interface for the arithmetic calculator."""
from __future__ import annotations

import argparse
import sys
from decimal import Decimal

from . import CalculationError, evaluate


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate arithmetic expressions containing +, -, *, /, and parentheses. "
            "Supports unary +/- and decimal numbers."
        )
    )
    parser.add_argument(
        "expression",
        nargs="*",
        help=(
            "Expression to evaluate. If omitted, the calculator starts an interactive "
            "prompt."
        ),
    )

    args = parser.parse_args(argv)

    if args.expression:
        expression = " ".join(args.expression)
        return _evaluate_and_display(expression)

    return _interactive_loop()


def _interactive_loop() -> int:
    print("Arithmetic calculator. Enter an expression or type 'exit' to quit.")
    while True:
        try:
            line = input("> ")
        except EOFError:
            print()
            return 0
        except KeyboardInterrupt:
            print()
            return 0

        if line.strip().lower() in {"exit", "quit"}:
            return 0
        if not line.strip():
            continue

        _evaluate_and_display(line)


def _evaluate_and_display(expression: str) -> int:
    try:
        result = evaluate(expression)
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        return 1
    except CalculationError as error:
        print(f"Error: {error}")
        return 1

    print(_format_decimal(result))
    return 0


def _format_decimal(value: Decimal) -> str:
    normalized = value.normalize()
    text = format(normalized, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


if __name__ == "__main__":  # pragma: no cover - module entry point guard
    sys.exit(main())
