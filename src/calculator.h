#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <stddef.h>

typedef enum {
    CALC_SUCCESS = 0,
    CALC_ERROR_INVALID_CHAR,
    CALC_ERROR_MALFORMED_EXPRESSION,
    CALC_ERROR_DIVISION_BY_ZERO,
    CALC_ERROR_TOO_MANY_TOKENS
} CalcStatus;

#define CALC_MAX_INPUT_LENGTH 255

int evaluate_expression(const char *expr, double *result, char *error, size_t error_size);

#endif /* CALCULATOR_H */
