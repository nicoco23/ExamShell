/* rotone */
/* Fonctions autorisees : write */

#include <unistd.h>

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	int		i = 0;
	char	c = av[1][i];

	while (av[1][i])
	{
		c = av[1][i];
		if (c >= 'a' && c <= 'z')
			c = (c - 'a' + 1) % 26 + 'a';
		if (c >= 'A' && c <= 'Z')
			c = (c - 'A' + 1) % 26 + 'A';
		write(1, &c, 1);
		i++;
	}
	return (write(1, "\n", 1), 0);
}
