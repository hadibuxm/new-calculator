# Arithmetic Calculator in C Programming

## Overview and Summary

This project aims to develop a reliable, user-friendly arithmetic calculator using the C programming language. The calculator will be able to perform basic mathematical operations including addition, subtraction, multiplication, and division. It is intended to serve as a useful tool for students and professionals who require quick and accurate mathematical computations.

## Key Decisions and Conclusions

- The calculator will be developed in C programming language, using a command line interface (CLI) for user interaction.
- It will support both integer and decimal numbers.
- The calculator will handle errors gracefully, providing appropriate error messages for situations like division by zero.
- The calculator will also be capable of handling multiple operations in a single input string, respecting the order of operations (PEMDAS/BODMAS).
- The priority of this feature is high, with no immediate dependencies identified.

## Important Details Discussed

- The calculator needs to use accurate data types to prevent potential loss of precision in calculations.
- Measures should be taken to prevent buffer overflow attacks by sanitizing user input and limiting input size.
- The calculator needs to be able to evaluate complex expressions. As C doesn't natively support this, a parser will need to be written or an existing library used.
- The importance of creating a well-structured and commented code was emphasized, to facilitate easier maintenance and future expansion of the program.

## Action Items or Next Steps

1. Define the project structure and main functions.
2. Implement the basic arithmetic operations (addition, subtraction, multiplication, division).
3. Create the CLI for user interaction.
4. Implement error handling for situations like division by zero.
5. Develop the functionality for handling multiple operations in a single input string.
6. Implement input sanitization and size limitation to prevent buffer overflow attacks.
7. Write or integrate a parser for evaluating complex expressions.
8. Test all parts of the code to ensure they function as expected.
9. Document the code properly for easier understanding and maintenance.

This project documentation will be updated as the development progresses. Contributions and suggestions for improvements are always welcome.