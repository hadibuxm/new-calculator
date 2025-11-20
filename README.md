# Arithmetic Calculator

A command-line arithmetic calculator written in C that evaluates expressions with support for parentheses and floating-point numbers. The parser respects operator precedence (PEMDAS) and reports errors for invalid input, including division by zero.

## Build

```sh
make
```

This produces the `calculator` executable in the project root.

## Usage

Run the program and enter an arithmetic expression. The calculator evaluates the input and prints the result. Submit an empty line or press `Ctrl+D` to exit.

```text
$ ./calculator
Arithmetic Calculator (enter blank line to exit)
> 2 + 3 * (4 - 1)
= 11
> 1 / 0
Error: Division by zero is not allowed.
> 
```

### Supported Features

- Addition, subtraction, multiplication, and division
- Parentheses to control evaluation order
- Integer and decimal operands (e.g., `3.14`, `-0.5`)
- Unary plus and minus (e.g., `-3 + 5`)
- Graceful error handling for malformed expressions and invalid operations

## Cleaning Up

```sh
make clean
```
