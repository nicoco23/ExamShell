/* snake_to_camel */
/* Fonctions autorisees : malloc, free, realloc, write */

#include <unistd.h>
#include <stdlib.h>

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	int		i = 0;
	char	c = av[1][i];
	while(av[1][i])
	{
		c = av[1][i];
		if (c == '_')
		{
			c = av[1][++i] - 32;
		}
		write(1, &c, 1);
		i++;
	}
	return (write(1, "\n", 1), 0);
}
