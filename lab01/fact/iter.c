/*
 * Calcula o factorial de forma iterativa.
 */

#include "fact.h"

int factorial(int n)
{
	int i, fact = 1;

	for (i = n; i > 0; i = i - 1)
		fact = fact * i;

	return fact;
}

