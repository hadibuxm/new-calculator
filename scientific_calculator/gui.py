"""Tkinter based graphical user interface for the scientific calculator."""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from . import operations as ops


class ScientificCalculatorApp:
    """Main application class wiring GUI controls to calculator operations."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.resizable(False, False)

        notebook = ttk.Notebook(root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self._init_basic_tab(notebook)
        self._init_scientific_tab(notebook)
        self._init_complex_tab(notebook)
        self._init_equation_tab(notebook)

    # ------------------------------------------------------------------
    # Basic
    def _init_basic_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Basic")

        ttk.Label(frame, text="Number A").grid(row=0, column=0, sticky=tk.W)
        self.basic_a_entry = ttk.Entry(frame, width=20)
        self.basic_a_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Number B").grid(row=1, column=0, sticky=tk.W)
        self.basic_b_entry = ttk.Entry(frame, width=20)
        self.basic_b_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Operation").grid(row=2, column=0, sticky=tk.W)
        self.basic_operation = tk.StringVar(value="Addition")
        operations = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
            "Modulus",
            "Exponentiation",
        ]
        ttk.Combobox(frame, textvariable=self.basic_operation, values=operations, state="readonly").grid(
            row=2, column=1, padx=5, pady=2
        )

        ttk.Button(frame, text="Compute", command=self._handle_basic_compute).grid(row=3, column=0, columnspan=2, pady=6)

        self.basic_result = tk.StringVar(value="Result: ")
        ttk.Label(frame, textvariable=self.basic_result, font=("Arial", 12, "bold")).grid(
            row=4, column=0, columnspan=2, sticky=tk.W
        )

    def _handle_basic_compute(self) -> None:
        try:
            a = self._parse_float(self.basic_a_entry.get(), "Number A")
            b = self._parse_float(self.basic_b_entry.get(), "Number B")
            operation = self.basic_operation.get()
            result = self._perform_basic_operation(operation, a, b)
            self.basic_result.set(f"Result: {result}")
        except ValueError as exc:
            messagebox.showerror("Input Error", str(exc))

    def _perform_basic_operation(self, operation: str, a: float, b: float) -> float:
        if operation == "Addition":
            return ops.add(a, b)
        if operation == "Subtraction":
            return ops.subtract(a, b)
        if operation == "Multiplication":
            return ops.multiply(a, b)
        if operation == "Division":
            return ops.divide(a, b)
        if operation == "Modulus":
            return ops.modulus(a, b)
        if operation == "Exponentiation":
            return ops.power(a, b)
        raise ValueError(f"Unsupported operation: {operation}")

    # ------------------------------------------------------------------
    # Scientific
    def _init_scientific_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Scientific")

        ttk.Label(frame, text="Value").grid(row=0, column=0, sticky=tk.W)
        self.scientific_value_entry = ttk.Entry(frame, width=20)
        self.scientific_value_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Nth value").grid(row=1, column=0, sticky=tk.W)
        self.nth_entry = ttk.Entry(frame, width=20)
        self.nth_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Operation").grid(row=2, column=0, sticky=tk.W)
        self.scientific_operation = tk.StringVar(value="Square Root")
        scientific_ops = [
            "Square Root",
            "Cube Root",
            "Nth Root",
            "Factorial",
            "Natural Logarithm",
            "Logarithm base 10",
            "Sine",
            "Cosine",
            "Tangent",
            "Arcsine",
            "Arccosine",
            "Arctangent",
            "Hyperbolic Sine",
            "Hyperbolic Cosine",
            "Hyperbolic Tangent",
            "Inverse Hyperbolic Sine",
            "Inverse Hyperbolic Cosine",
            "Inverse Hyperbolic Tangent",
            "Exponential",
            "Absolute Value",
        ]
        ttk.Combobox(frame, textvariable=self.scientific_operation, values=scientific_ops, state="readonly").grid(
            row=2, column=1, padx=5, pady=2
        )

        self.angle_in_degrees = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame, text="Use degrees for trig functions", variable=self.angle_in_degrees).grid(
            row=3, column=0, columnspan=2, sticky=tk.W
        )

        ttk.Button(frame, text="Compute", command=self._handle_scientific_compute).grid(
            row=4, column=0, columnspan=2, pady=6
        )

        self.scientific_result = tk.StringVar(value="Result: ")
        ttk.Label(frame, textvariable=self.scientific_result, font=("Arial", 12, "bold")).grid(
            row=5, column=0, columnspan=2, sticky=tk.W
        )

        ttk.Label(
            frame,
            text="Note: 'Nth value' is only required for the Nth Root operation.",
            font=("Arial", 9),
        ).grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=(8, 0))

    def _handle_scientific_compute(self) -> None:
        try:
            value = self._parse_float(self.scientific_value_entry.get(), "Value")
            operation = self.scientific_operation.get()
            use_degrees = self.angle_in_degrees.get()
            result = self._perform_scientific_operation(operation, value, use_degrees)
            self.scientific_result.set(f"Result: {result}")
        except ValueError as exc:
            messagebox.showerror("Input Error", str(exc))

    def _perform_scientific_operation(self, operation: str, value: float, use_degrees: bool) -> float:
        if operation == "Square Root":
            return ops.square_root(value)
        if operation == "Cube Root":
            return ops.cube_root(value)
        if operation == "Nth Root":
            n_value = self._parse_int(self.nth_entry.get(), "Nth value")
            return ops.nth_root(value, n_value)
        if operation == "Factorial":
            int_value = self._parse_int(self.scientific_value_entry.get(), "Value")
            return ops.factorial(int_value)
        if operation == "Natural Logarithm":
            return ops.natural_log(value)
        if operation == "Logarithm base 10":
            return ops.log_base_10(value)
        if operation == "Sine":
            return ops.sine(value, degrees=use_degrees)
        if operation == "Cosine":
            return ops.cosine(value, degrees=use_degrees)
        if operation == "Tangent":
            return ops.tangent(value, degrees=use_degrees)
        if operation == "Arcsine":
            return ops.arcsine(value, degrees=use_degrees)
        if operation == "Arccosine":
            return ops.arccosine(value, degrees=use_degrees)
        if operation == "Arctangent":
            return ops.arctangent(value, degrees=use_degrees)
        if operation == "Hyperbolic Sine":
            return ops.hyperbolic_sine(value)
        if operation == "Hyperbolic Cosine":
            return ops.hyperbolic_cosine(value)
        if operation == "Hyperbolic Tangent":
            return ops.hyperbolic_tangent(value)
        if operation == "Inverse Hyperbolic Sine":
            return ops.inverse_hyperbolic_sine(value)
        if operation == "Inverse Hyperbolic Cosine":
            return ops.inverse_hyperbolic_cosine(value)
        if operation == "Inverse Hyperbolic Tangent":
            return ops.inverse_hyperbolic_tangent(value)
        if operation == "Exponential":
            return ops.exponential(value)
        if operation == "Absolute Value":
            return ops.absolute_value(value)
        raise ValueError(f"Unsupported operation: {operation}")

    # ------------------------------------------------------------------
    # Complex
    def _init_complex_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Complex")

        ttk.Label(frame, text="Complex Z1 (e.g. 3+4i)").grid(row=0, column=0, sticky=tk.W)
        self.complex_z1_entry = ttk.Entry(frame, width=25)
        self.complex_z1_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Complex Z2 (e.g. 1-2i)").grid(row=1, column=0, sticky=tk.W)
        self.complex_z2_entry = ttk.Entry(frame, width=25)
        self.complex_z2_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Operation").grid(row=2, column=0, sticky=tk.W)
        self.complex_operation = tk.StringVar(value="Addition")
        complex_ops = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
            "Magnitude (Z1)",
            "Argument (Z1)",
            "Conjugate (Z1)",
        ]
        ttk.Combobox(frame, textvariable=self.complex_operation, values=complex_ops, state="readonly").grid(
            row=2, column=1, padx=5, pady=2
        )

        ttk.Button(frame, text="Compute", command=self._handle_complex_compute).grid(
            row=3, column=0, columnspan=2, pady=6
        )

        self.complex_result = tk.StringVar(value="Result: ")
        ttk.Label(frame, textvariable=self.complex_result, font=("Arial", 12, "bold")).grid(
            row=4, column=0, columnspan=2, sticky=tk.W
        )

        ttk.Label(
            frame,
            text="Note: Magnitude, Argument, and Conjugate use Z1 only.",
            font=("Arial", 9),
        ).grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=(8, 0))

    def _handle_complex_compute(self) -> None:
        try:
            z1 = self._parse_complex(self.complex_z1_entry.get(), "Complex Z1")
            operation = self.complex_operation.get()
            if operation in {"Addition", "Subtraction", "Multiplication", "Division"}:
                z2 = self._parse_complex(self.complex_z2_entry.get(), "Complex Z2")
                result = self._perform_complex_binary(operation, z1, z2)
            else:
                result = self._perform_complex_unary(operation, z1)
            self.complex_result.set(f"Result: {result}")
        except ValueError as exc:
            messagebox.showerror("Input Error", str(exc))

    def _perform_complex_binary(self, operation: str, z1: complex, z2: complex) -> complex:
        if operation == "Addition":
            return ops.complex_add(z1, z2)
        if operation == "Subtraction":
            return ops.complex_subtract(z1, z2)
        if operation == "Multiplication":
            return ops.complex_multiply(z1, z2)
        if operation == "Division":
            return ops.complex_divide(z1, z2)
        raise ValueError(f"Unsupported complex operation: {operation}")

    def _perform_complex_unary(self, operation: str, z: complex):
        if operation == "Magnitude (Z1)":
            return ops.complex_magnitude(z)
        if operation == "Argument (Z1)":
            return ops.complex_argument(z)
        if operation == "Conjugate (Z1)":
            return ops.complex_conjugate(z)
        raise ValueError(f"Unsupported complex operation: {operation}")

    # ------------------------------------------------------------------
    # Equations
    def _init_equation_tab(self, notebook: ttk.Notebook) -> None:
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Equations")

        ttk.Label(frame, text="Coefficient a").grid(row=0, column=0, sticky=tk.W)
        self.eq_a_entry = ttk.Entry(frame, width=20)
        self.eq_a_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Coefficient b").grid(row=1, column=0, sticky=tk.W)
        self.eq_b_entry = ttk.Entry(frame, width=20)
        self.eq_b_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Coefficient c").grid(row=2, column=0, sticky=tk.W)
        self.eq_c_entry = ttk.Entry(frame, width=20)
        self.eq_c_entry.grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Equation Type").grid(row=3, column=0, sticky=tk.W)
        self.equation_type = tk.StringVar(value="Linear")
        types = ["Linear", "Quadratic"]
        ttk.Combobox(frame, textvariable=self.equation_type, values=types, state="readonly").grid(
            row=3, column=1, padx=5, pady=2
        )

        ttk.Button(frame, text="Solve", command=self._handle_equation_solve).grid(
            row=4, column=0, columnspan=2, pady=6
        )

        self.equation_result = tk.StringVar(value="Result: ")
        ttk.Label(frame, textvariable=self.equation_result, font=("Arial", 12, "bold")).grid(
            row=5, column=0, columnspan=2, sticky=tk.W
        )

        ttk.Label(
            frame,
            text="For linear equations enter coefficients for ax + b = 0. For quadratic enter ax^2 + bx + c = 0.",
            font=("Arial", 9),
            wraplength=320,
        ).grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=(8, 0))

    def _handle_equation_solve(self) -> None:
        try:
            a = self._parse_float(self.eq_a_entry.get(), "Coefficient a")
            b = self._parse_float(self.eq_b_entry.get(), "Coefficient b")
            equation_type = self.equation_type.get()
            if equation_type == "Linear":
                result = ops.solve_linear(a, b)
            else:
                c = self._parse_float(self.eq_c_entry.get(), "Coefficient c")
                roots = ops.solve_quadratic(a, b, c)
                result = f"x1 = {roots[0]}, x2 = {roots[1]}"
                self.equation_result.set(f"Result: {result}")
                return
            self.equation_result.set(f"Result: {result}")
        except ValueError as exc:
            messagebox.showerror("Input Error", str(exc))

    # ------------------------------------------------------------------
    # Helpers
    def _parse_float(self, value: str, label: str) -> float:
        try:
            return float(value)
        except ValueError as exc:
            raise ValueError(f"{label} must be a number.") from exc

    def _parse_int(self, value: str, label: str) -> int:
        try:
            if value.strip() == "":
                raise ValueError
            return int(value)
        except ValueError as exc:
            raise ValueError(f"{label} must be an integer.") from exc

    def _parse_complex(self, value: str, label: str) -> complex:
        text = value.strip()
        if not text:
            raise ValueError(f"{label} is required.")
        text = text.replace("i", "j").replace("I", "j")
        try:
            return complex(text)
        except ValueError as exc:
            raise ValueError(f"{label} must be a complex number (e.g. 3+4i).") from exc


def launch_app() -> None:
    """Create the Tk root window and start the calculator application."""
    root = tk.Tk()
    ScientificCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    launch_app()
