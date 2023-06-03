#include <stdio.h>

/*
 * Finds the smallest divisor, if any, of a given number.
 * Return: smallest divisor if found, or 0 if the number is prime.
 */
int trial_division(long int n)
{
	long int factor;

	if (n % 2 == 0)
	{
		printf("%lu=%lu*%i\n", n, n / 2, 2);
		return 0;
	}

	factor = 3;
	while (factor * factor <= n)
	{
		if (n % factor == 0)
		{
			printf("%lu=%lu*%lu\n", n, n / factor, factor);
			return 0;
		}
		else
			factor += 2;
	}

	printf("%lu=%lu*%i\n", n, n, 1);

	return 0;
}