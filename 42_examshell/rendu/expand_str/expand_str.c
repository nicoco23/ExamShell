/* expand_str */
/* Fonctions autorisees : write */

#include <unistd.h>

int	is_space(char c)
{
	if (c == 32 ||(c >= 7 && c <= 13))
		return (1);
	else
		return (0);
}

void	normalize(char *str)
{
	int		space = 0;
	int		i = 0;
	char	c;

	while (str[i])
	{
		c = str[i];
		if (is_space(c) == 0)
		{
			write(1, &c, 1);
			i++;
		}
		else
		{
			space = 1;
			i++;
		}
		if (space == 1)
		{
			write(1, "   ", 3);
			space = 0;
		}
	}
}

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	normalize(av[1]);
	return (write(1, "\n", 1), 0);
}
