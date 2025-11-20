# Arithmetic Calculator in Python

## 1. Overview and Summary

This project aims to develop a reliable, user-friendly arithmetic calculator using Python. The calculator will be capable of performing basic mathematical operations, including addition, subtraction, multiplication, and division. It will cater to the needs of students and professionals who require a quick and accurate tool for basic arithmetic calculations.

## 2. Key Decisions and Conclusions

- The calculator will be developed using Python, a high-level language known for its extensive library support and readability.
- The calculator will handle and display input and output of both integers and decimal numbers.
- Error handling will be implemented for scenarios such as division by zero.
- The calculator will be able to handle multiple operations in a single input string, respecting the order of operations (PEMDAS/BODMAS).
- The user interface will be clear and user-friendly, providing clear instructions for input.

## 3. Important Details Discussed

- Python's inbuilt `eval()` function could be utilized for evaluating expressions. However, user input should be sanitized to prevent code injection attacks.
- The use of libraries such as Tkinter or PyQt could be considered for developing a GUI application. Alternatively, a CLI could be used.
- The code should be structured in an object-oriented manner using classes and methods. This will facilitate easier maintenance and expansion in the future.
- Test-driven development is recommended to ensure all parts of the code function as expected.

## 4. Action Items or Next Steps

- **Research**: Investigate further on Python's `eval()` function and the potential security risks associated with it.
- **Design**: Decide on the user interface - GUI or CLI. If GUI, choose between Tkinter and PyQt.
- **Development**: Begin coding the calculator, ensuring to follow best practices for Python and object-oriented design.
- **Testing**: Implement test-driven development. Write tests for each function as it's developed and perform regular testing and debugging.
- **Documentation**: Continue updating this document as the project progresses, adding any new decisions or important information.