#include "calculator.h"

#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define ERROR_BUFFER_SIZE 128

static void flush_stdin_line(void)
{
    int ch = 0;
    while ((ch = getchar()) != '\n' && ch != EOF) {
        ;
    }
}

static void trim(char *text)
{
    if (!text) {
        return;
    }

    char *start = text;
    while (*start && isspace((unsigned char)*start)) {
        start++;
    }

    char *end = start + strlen(start);
    while (end > start && isspace((unsigned char)*(end - 1))) {
        end--;
    }
    *end = '\0';

    if (start != text) {
        memmove(text, start, (size_t)(end - start + 1));
    }
}

int main(void)
{
    char buffer[CALC_MAX_INPUT_LENGTH + 2];

    puts("Arithmetic Calculator (type 'exit' or 'quit' to close)");

    for (;;) {
        fputs("> ", stdout);
        fflush(stdout);

        if (!fgets(buffer, sizeof(buffer), stdin)) {
            putchar('\n');
            break;
        }

        if (strchr(buffer, '\n') == NULL) {
            flush_stdin_line();
            printf("Error: Input exceeds %d characters.\n", CALC_MAX_INPUT_LENGTH);
            continue;
        }

        buffer[strcspn(buffer, "\n")] = '\0';
        trim(buffer);

        if (buffer[0] == '\0') {
            continue;
        }

        if (strcmp(buffer, "exit") == 0 || strcmp(buffer, "quit") == 0) {
            puts("Goodbye.");
            break;
        }

        double result = 0.0;
        char error[ERROR_BUFFER_SIZE];
        int status = evaluate_expression(buffer, &result, error, sizeof(error));

        if (status == CALC_SUCCESS) {
            printf("= %.10g\n", result);
        } else {
            printf("%s\n", error);
        }
    }

    return 0;
}
