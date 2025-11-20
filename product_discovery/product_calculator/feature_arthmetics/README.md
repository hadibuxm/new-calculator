# Arithmetic Calculator in C Programming

## Overview and Summary

The purpose of this project is to develop a reliable, user-friendly arithmetic calculator using C programming language. The calculator will perform basic mathematical operations including addition, subtraction, multiplication, and division. It will cater to the needs of students and professionals who require a quick and accurate tool for basic calculations.

## Key Decisions and Conclusions

The calculator will be designed with a command line interface (CLI) for ease of use and compatibility with the C programming language. It will handle both integers and decimal numbers, and multiple operations in a single input string, while respecting the order of operations (PEMDAS/BODMAS).

The calculator will handle errors gracefully, such as dividing by zero, and will return appropriate error messages in such cases. High priority is given to this feature due to its fundamental utility.

## Important Details Discussed

The project will leverage the C programming language, and it's important to use accurate data types to prevent potential loss of precision in calculations. Care should be taken to prevent buffer overflow attacks by sanitizing user input and limiting input size.

The C language does not natively support evaluation of complex expressions, so we will need to write a parser or use an existing library for this. The code should be well-structured and commented for ease of maintenance and future expansion.

## Action Items or Next Steps

1. **Design Phase**: Sketch out the design of the calculator, including user interface and functionality.
2. **Development Phase**: Start the development of the calculator in C programming language, ensuring to implement the features discussed above.
3. **Testing Phase**: Conduct rigorous testing to ensure all parts of the code function as expected. This includes handling of both integer and decimal numbers, correct operation order, and error handling.
4. **Documentation Phase**: Document all functions, algorithms, and data structures used in the code for future reference and maintenance.
5. **Deployment Phase**: After successful testing, deploy the calculator for use.

This README will be updated as the project progresses and more details become available.