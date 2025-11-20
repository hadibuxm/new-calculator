CC := cc
CFLAGS := -std=c11 -Wall -Wextra -Werror -pedantic -O2
LDFLAGS := -lm

SRC := src/main.c src/calculator.c

.PHONY: all clean

all: calculator

calculator: $(SRC)
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f calculator
