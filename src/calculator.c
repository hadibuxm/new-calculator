#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT_LENGTH 256
#define ERROR_BUFFER_SIZE 128
#define ZERO_EPSILON 1e-12

typedef struct {
    const char *input;
    size_t position;
    char error[ERROR_BUFFER_SIZE];
} Parser;

static void set_error(Parser *parser, const char *message) {
    if (parser->error[0] == '\0') {
        snprintf(parser->error, sizeof(parser->error), "%s", message);
    }
}

static void skip_whitespace(Parser *parser) {
    while (parser->input[parser->position] != '\0' && isspace((unsigned char)parser->input[parser->position])) {
        parser->position++;
    }
}

static double parse_expression(Parser *parser, bool *ok);
static double parse_term(Parser *parser, bool *ok);
static double parse_unary(Parser *parser, bool *ok);
static double parse_primary(Parser *parser, bool *ok);

static double parse_expression(Parser *parser, bool *ok) {
    double value = parse_term(parser, ok);

    while (*ok) {
        skip_whitespace(parser);
        char op = parser->input[parser->position];

        if (op != '+' && op != '-') {
            break;
        }

        parser->position++;
        double rhs = parse_term(parser, ok);
        if (!*ok) {
            return 0.0;
        }

        if (op == '+') {
            value += rhs;
        } else {
            value -= rhs;
        }
    }

    return value;
}

static double parse_term(Parser *parser, bool *ok) {
    double value = parse_unary(parser, ok);

    while (*ok) {
        skip_whitespace(parser);
        char op = parser->input[parser->position];

        if (op != '*' && op != '/') {
            break;
        }

        parser->position++;
        double rhs = parse_unary(parser, ok);
        if (!*ok) {
            return 0.0;
        }

        if (op == '*') {
            value *= rhs;
        } else {
            if (fabs(rhs) < ZERO_EPSILON) {
                set_error(parser, "Division by zero is not allowed.");
                *ok = false;
                return 0.0;
            }
            value /= rhs;
        }
    }

    return value;
}

static double parse_unary(Parser *parser, bool *ok) {
    skip_whitespace(parser);
    char op = parser->input[parser->position];

    if (op == '+' || op == '-') {
        parser->position++;
        double value = parse_unary(parser, ok);
        if (!*ok) {
            return 0.0;
        }
        return (op == '-') ? -value : value;
    }

    return parse_primary(parser, ok);
}

static double parse_primary(Parser *parser, bool *ok) {
    skip_whitespace(parser);
    char current = parser->input[parser->position];

    if (current == '\0') {
        set_error(parser, "Unexpected end of expression.");
        *ok = false;
        return 0.0;
    }

    if (current == '(') {
        parser->position++;
        double value = parse_expression(parser, ok);
        if (!*ok) {
            return 0.0;
        }

        skip_whitespace(parser);
        if (parser->input[parser->position] != ')') {
            set_error(parser, "Missing closing parenthesis.");
            *ok = false;
            return 0.0;
        }
        parser->position++;
        return value;
    }

    if (isdigit((unsigned char)current) || current == '.') {
        char *end_ptr = NULL;
        double value = strtod(parser->input + parser->position, &end_ptr);
        if (end_ptr == parser->input + parser->position) {
            set_error(parser, "Invalid number format.");
            *ok = false;
            return 0.0;
        }

        parser->position = (size_t)(end_ptr - parser->input);
        return value;
    }

    set_error(parser, "Unexpected character in expression.");
    *ok = false;
    return 0.0;
}

static bool parse_and_evaluate(const char *expression, double *result, char *error_buffer, size_t error_buffer_size) {
    Parser parser = {
        .input = expression,
        .position = 0
    };
    parser.error[0] = '\0';

    bool ok = true;
    double value = parse_expression(&parser, &ok);

    if (ok) {
        skip_whitespace(&parser);
        if (parser.input[parser.position] != '\0' && parser.input[parser.position] != '\n') {
            set_error(&parser, "Unexpected trailing characters in expression.");
            ok = false;
        }
    }

    if (!ok) {
        if (error_buffer != NULL && error_buffer_size > 0) {
            snprintf(error_buffer, error_buffer_size, "%s", parser.error[0] ? parser.error : "Unable to evaluate expression.");
        }
        return false;
    }

    *result = value;
    if (error_buffer != NULL && error_buffer_size > 0) {
        error_buffer[0] = '\0';
    }
    return true;
}

int main(void) {
    char input[MAX_INPUT_LENGTH];

    printf("Arithmetic Calculator (enter blank line to exit)\n");

    while (1) {
        printf("> ");
        if (fgets(input, sizeof(input), stdin) == NULL) {
            putchar('\n');
            break;
        }

        if (input[0] == '\n' || input[0] == '\0') {
            break;
        }

        double result = 0.0;
        char error[ERROR_BUFFER_SIZE];

        if (parse_and_evaluate(input, &result, error, sizeof(error))) {
            printf("= %.10g\n", result);
        } else {
            fprintf(stderr, "Error: %s\n", error);
        }
    }

    return 0;
}
