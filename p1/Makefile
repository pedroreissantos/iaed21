CC=gcc
CFLAGS=-Wall -Wextra -Werror -ansi -pedantic -g
all:: proj1
	$(MAKE) $(MFLAGS) -C tests
proj1: proj1.c
clean::
	rm -f proj1 a.out *.o core tests/*.diff
