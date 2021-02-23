#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
	int a = 0, b = 1, n = 46, i = n;
	 if (argc > 1)
		i = n = atoi(argv[1]);
	 while (--i) {
		int t = a + b;
		a = b;
		b = t;
	}
	printf("fib(%d)=%d\n", n, b);
	return 0;
}
