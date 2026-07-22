/* repeat_alpha */
/* Fonctions autorisees : write */

#include <unistd.h>

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	int		i = 0;
	char	c;
	int		rep = 0;

	while (av[1][i])
	{
		rep = -1;
		c = av[1][i++];
		if (c >= 'a' && c <= 'z')
			rep = c - 'a';
		else if (c >= 'A' && c <= 'Z')
			rep = c - 'A';
		if (rep == -1)
			write(1, &c, 1);
		while (rep-- >= 0)
			write(1, &c, 1);
	}
	return (write(1, "\n", 1), 0);
}
