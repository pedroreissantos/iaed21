#include <stdio.h>		/* for printf */
#include <stdlib.h>		/* for atoi */

int fib(int n) {
	if (n < 2)
		return n;
	return fib(n - 2) + fib(n - 1);
}

int main(int argc, char *argv[]) {
	int n = 42;

	if (argc > 1)
		n = atoi(argv[1]);

	printf("fib(%d)=%d\n", n, fib(n));
	return 0;
}
