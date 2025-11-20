# Arithmetic Calculator

A safe, user-friendly arithmetic calculator implemented in Python. It evaluates expressions that use addition, subtraction, multiplication, division, and parentheses while respecting the standard order of operations.

## Features
- Handles integers and decimal numbers seamlessly.
- Supports chained expressions and nested parentheses using PEMDAS/BODMAS rules.
- Protects against unsafe input by allowing only basic arithmetic tokens.
- Provides clear error messages for invalid input, including division by zero.
- Includes both a reusable Python class and an interactive CLI.

## Getting Started

### Prerequisites
- Python 3.9 or later (earlier 3.x versions may also work).

### CLI Usage
Run the calculator from the project root:

```bash
python main.py
```

Example session:

```
Arithmetic Calculator
Enter an expression using +, -, *, /, and parentheses.
Type 'quit' to exit.

> 2 + 3 * 4
Result: 14
> (2 + 3) * 4
Result: 20
> quit
Goodbye!
```

### Programmatic Use

```python
from calculator import ArithmeticCalculator

calc = ArithmeticCalculator()
print(calc.evaluate("(5 + 3) / 2"))  # 4.0
```

## Testing
Run the automated test suite with:

```bash
python -m unittest discover tests
```

The tests cover the four basic operations, mixed expressions, decimal arithmetic, error handling, and input validation.
