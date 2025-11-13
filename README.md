# Scientific Calculator

A cross-functional scientific calculator built with Python and Tkinter. The application supports basic arithmetic, advanced scientific functions, complex number operations, and equation solving through an intuitive graphical interface.

## Features

- **Basic arithmetic:** addition, subtraction, multiplication, division, modulus, and exponentiation.
- **Scientific functions:** square, cube, and nth roots; factorial; natural and base-10 logarithms; trigonometric, inverse trigonometric, hyperbolic, and inverse hyperbolic functions; exponential; and absolute value operations.
- **Complex numbers:** addition, subtraction, multiplication, division, magnitude, argument, and conjugation.
- **Equation solving:** linear equations of the form `ax + b = 0` and quadratic equations of the form `ax² + bx + c = 0` with support for complex solutions.
- **Error handling:** clear validation and messaging for invalid inputs or undefined operations.

## Getting Started

### Prerequisites

- Python 3.9 or later (standard library only; no external dependencies).

### Running the Application

```bash
python main.py
```

The GUI will open in a new window. Select the desired tab (Basic, Scientific, Complex, or Equations), provide the required inputs, and click **Compute**/**Solve** to view results.

### Running Tests

Automated tests cover the core calculation functions:

```bash
python -m unittest discover -s tests
```

## Project Structure

```
.
├── main.py                         # CLI entry point
├── scientific_calculator
│   ├── __init__.py                 # Package export for launch_app
│   ├── gui.py                      # Tkinter-based user interface
│   └── operations.py               # Core calculation functions
└── tests
    └── test_operations.py          # Unit tests for operations
```

## Future Improvements

- Add keyboard shortcuts and history tracking within the GUI.
- Provide theming support (light/dark mode) and accessibility enhancements.
- Extend equation solving to systems of equations and higher-order polynomials.

## License

This project is provided as-is for educational purposes.
