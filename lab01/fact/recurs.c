/*
 * Calcula o factorial de forma recursiva.
 */
#include "fact.h"

int factorial (int n)
{
	int fact;

	if(n == 0)
		fact = 1;
	else
		fact = n * factorial(n - 1);

	return fact;
}
