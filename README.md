# Arithmetic Calculator

A lightweight command-line calculator implemented in C. It evaluates arithmetic expressions with support for parentheses, operator precedence (PEMDAS/BODMAS), and both integer and floating-point values.

## Features
- Addition, subtraction, multiplication, and division for integers and decimals.
- Full precedence handling with nested parentheses and unary operators.
- Graceful error reporting for malformed expressions and division by zero.
- Input sanitisation and a fixed maximum length (255 characters) to mitigate buffer overflow risks.

## Build
```sh
make
```
This produces an executable named `calculator` in the repository root.

## Usage
Run the executable and enter expressions when prompted. Type `exit` or `quit` to leave the program.
```text
$ ./calculator
Arithmetic Calculator (type 'exit' or 'quit' to close)
> 12 / (2 + 4) * 3.5
= 7
> -5 + 3 * (2.4 - 6)
= -8.2
> quit
Goodbye.
```

## Implementation Notes
- The expression evaluator uses a recursive-descent parser to honour operator precedence without relying on external libraries.
- Division by values with absolute magnitude below `1e-12` is treated as division by zero to avoid floating-point precision pitfalls.
- Input is read with `fgets` into a bounded buffer; excess characters are discarded before evaluation.
- Only digits, whitespace, parentheses, decimal separators, operators, and optional scientific notation markers (`e`/`E`) are accepted.

## Cleaning Up
Remove the compiled binary with:
```sh
make clean
```
