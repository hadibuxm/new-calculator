"""Command-line interface for the arithmetic calculator."""

from __future__ import annotations

from calculator import ArithmeticCalculator, CalculatorError


def main() -> None:
    calculator = ArithmeticCalculator()
    print("Arithmetic Calculator")
    print("Enter an expression using +, -, *, /, and parentheses.")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            expression = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if expression.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            return

        if not expression:
            print("Please enter an expression or 'quit' to exit.")
            continue

        try:
            result = calculator.evaluate(expression)
        except CalculatorError as error:
            print(f"Error: {error}")
        else:
            print(f"Result: {result}")


if __name__ == "__main__":
    main()
