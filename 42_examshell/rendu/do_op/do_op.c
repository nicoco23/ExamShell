/* do_op */
/* Fonctions autorisees : atoi, printf, write */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int	main(int ac, char **av)
{
	if (ac != 4)
		return (write(1, "\n", 1), 0);
	int		a = atoi(av[1]);
	char	b = av[2][0];
	int		c = atoi(av[3]);
	int		res;
	if (b == '+')
		res = a + c;
	else if (b == '-')
		res = a - c;
	else if (b == '*')
		res = a * c;
	else if (b == '%')
		res = a % c;
	else if (b == '/')
		res = a / c;
	printf("%d\n", res);
	return (0);
}
