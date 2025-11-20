#include "calculator.h"

#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define EPSILON 1e-12

static void skip_spaces(const char **expr)
{
    while (**expr && isspace((unsigned char)**expr)) {
        (*expr)++;
    }
}

static int sanitize_input(const char *expr, char *error, size_t error_size)
{
    for (size_t i = 0; expr[i] != '\0'; i++) {
        unsigned char c = (unsigned char)expr[i];
        if (isspace(c)) {
            continue;
        }
        if ((c >= '0' && c <= '9') || c == '+' || c == '-' || c == '*' || c == '/' || c == '.' ||
            c == '(' || c == ')' || c == 'e' || c == 'E') {
            continue;
        }
        if (error && error_size > 0) {
            snprintf(error, error_size, "Error: Unsupported character '%c'.", c);
        }
        return CALC_ERROR_INVALID_CHAR;
    }
    return CALC_SUCCESS;
}

static int parse_expression(const char **expr, double *result, char *error, size_t error_size);

static int parse_factor(const char **expr, double *result, char *error, size_t error_size)
{
    skip_spaces(expr);
    char current = **expr;

    if (current == '+' || current == '-') {
        (*expr)++;
        double inner = 0.0;
        int status = parse_factor(expr, &inner, error, error_size);
        if (status != CALC_SUCCESS) {
            return status;
        }
        *result = (current == '-') ? -inner : inner;
        return CALC_SUCCESS;
    }

    if (current == '(') {
        (*expr)++;
        double inner = 0.0;
        int status = parse_expression(expr, &inner, error, error_size);
        if (status != CALC_SUCCESS) {
            return status;
        }
        skip_spaces(expr);
        if (**expr != ')') {
            if (error && error_size > 0) {
                snprintf(error, error_size, "Error: Missing closing parenthesis.");
            }
            return CALC_ERROR_MALFORMED_EXPRESSION;
        }
        (*expr)++;
        *result = inner;
        return CALC_SUCCESS;
    }

    char *endptr = NULL;
    double value = strtod(*expr, &endptr);
    if (endptr == *expr) {
        if (error && error_size > 0) {
            snprintf(error, error_size, "Error: Invalid number in expression.");
        }
        return CALC_ERROR_MALFORMED_EXPRESSION;
    }
    *expr = endptr;
    *result = value;
    return CALC_SUCCESS;
}

static int parse_term(const char **expr, double *result, char *error, size_t error_size)
{
    double value = 0.0;
    int status = parse_factor(expr, &value, error, error_size);
    if (status != CALC_SUCCESS) {
        return status;
    }

    while (1) {
        skip_spaces(expr);
        char current = **expr;
        if (current != '*' && current != '/') {
            break;
        }
        (*expr)++;

        double rhs = 0.0;
        status = parse_factor(expr, &rhs, error, error_size);
        if (status != CALC_SUCCESS) {
            return status;
        }

        if (current == '*') {
            value *= rhs;
        } else {
            if (fabs(rhs) < EPSILON) {
                if (error && error_size > 0) {
                    snprintf(error, error_size, "Error: Division by zero.");
                }
                return CALC_ERROR_DIVISION_BY_ZERO;
            }
            value /= rhs;
        }
    }

    *result = value;
    return CALC_SUCCESS;
}

static int parse_expression(const char **expr, double *result, char *error, size_t error_size)
{
    double value = 0.0;
    int status = parse_term(expr, &value, error, error_size);
    if (status != CALC_SUCCESS) {
        return status;
    }

    while (1) {
        skip_spaces(expr);
        char current = **expr;
        if (current != '+' && current != '-') {
            break;
        }
        (*expr)++;

        double rhs = 0.0;
        status = parse_term(expr, &rhs, error, error_size);
        if (status != CALC_SUCCESS) {
            return status;
        }

        if (current == '+') {
            value += rhs;
        } else {
            value -= rhs;
        }
    }

    *result = value;
    return CALC_SUCCESS;
}

int evaluate_expression(const char *expr, double *result, char *error, size_t error_size)
{
    if (!expr || !result) {
        if (error && error_size > 0) {
            snprintf(error, error_size, "Error: Invalid arguments provided.");
        }
        return CALC_ERROR_MALFORMED_EXPRESSION;
    }

    if (strlen(expr) > CALC_MAX_INPUT_LENGTH) {
        if (error && error_size > 0) {
            snprintf(error, error_size, "Error: Expression exceeds %d characters.", CALC_MAX_INPUT_LENGTH);
        }
        return CALC_ERROR_MALFORMED_EXPRESSION;
    }

    int status = sanitize_input(expr, error, error_size);
    if (status != CALC_SUCCESS) {
        return status;
    }

    const char *cursor = expr;
    skip_spaces(&cursor);
    if (*cursor == '\0') {
        if (error && error_size > 0) {
            snprintf(error, error_size, "Error: Expression is empty.");
        }
        return CALC_ERROR_MALFORMED_EXPRESSION;
    }

    double value = 0.0;
    status = parse_expression(&cursor, &value, error, error_size);
    if (status != CALC_SUCCESS) {
        return status;
    }

    skip_spaces(&cursor);
    if (*cursor != '\0') {
        if (error && error_size > 0) {
            snprintf(error, error_size, "Error: Unexpected character '%c'.", *cursor);
        }
        return CALC_ERROR_MALFORMED_EXPRESSION;
    }

    *result = value;
    return CALC_SUCCESS;
}
