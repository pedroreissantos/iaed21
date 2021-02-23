#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
	long long a = 0, b = 1, n = 92, i = n;
	 if (argc > 1)
		i = n = atoi(argv[1]);
	 while (--i) {
		long long t = a + b;
		a = b;
		b = t;
	}
	printf("fib(%lld)=%lld\n", n, b);
	return 0;
}
