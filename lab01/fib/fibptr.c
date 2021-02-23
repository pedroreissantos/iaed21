#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
	int n = 42, i = 0, j = 1, *seg = &i;
	if (argc > 1)
		n = atoi(argv[1]);
	while (n-- > 0) {
		seg[0] = i + j;
		seg = (seg == &i) ? &j : &i;
	}
	printf("%d\n", seg[0]);
	return 0;
}
