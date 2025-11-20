# new-calculator

## Arithmetic Calculator (Python)

This project provides a command-line arithmetic calculator capable of evaluating
expressions containing addition, subtraction, multiplication, division,
parentheses, unary operators, integers, and decimal numbers. Expressions are
parsed safely without relying on Python's `eval`, and results are produced with
`Decimal` precision to avoid common floating point issues.

### Running the calculator

```bash
python -m calculator "2 + 3 * 4"
```

Omitting the expression starts an interactive prompt:

```bash
python -m calculator
```

Type an expression and press Enter to see the result. Use `exit` or `quit` to
leave the prompt.

### Running the tests

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

### Repository structure

- `calculator/` – calculator package and CLI entry point.
- `tests/` – unit tests covering the expression evaluator.
- `product_discovery/` – original ideation artifacts that informed this
  implementation.
