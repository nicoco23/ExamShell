/* alpha_mirror */
/* Fonctions autorisees : write */

#include <unistd.h>

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	int		i = 0;
	char	c;

	while (av[1][i])
	{
		c = av[1][i];
		if (c >= 'a' && c <= 'z')
			c = 'z' - (c - 'a');
		else if (c >= 'A' && c <= 'Z')
			c = 'Z' - (c - 'A');
		write(1, &c, 1);
		i++;
	}
	return (write(1, "\n", 1), 0);
}
