/* repeat_alpha */
/* Fonctions autorisees : write */

#include <unistd.h>

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	int		i = 0;
	int		rep;
	char	c;

	while (av[1][i])
	{
		rep = 0;
		c = av[1][i];
		if (c >= 'a' && c <= 'z')
			rep = c - 'a';
		else if (c >= 'A' && c <= 'Z')
			rep = c - 'A';
		while (rep-- >= 0)
			write(1, &c, 1);
		i++;
	}
	return (write(1, "\n", 1), 0);
}
