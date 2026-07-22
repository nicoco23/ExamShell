/* rot_13 */
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
			c = (c + 13 - 'a') % 26 + 'a';
		else if (c >= 'A' && c <= 'Z')
			c = (c + 13 - 'A') % 26 + 'A';
		write(1, &c, 1);
		i++;
	}
	return (write(1, "\n", 1), 0);
}
