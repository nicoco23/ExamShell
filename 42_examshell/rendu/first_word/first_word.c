/* first_word */
/* Fonctions autorisees : write */

#include <unistd.h>

int	is_space(char c)
{
	if (c == 32 || (c >= 7 && c <= 13))
		return (1);
	else 
		return (0);
}

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	int		i = 0;
	while (av[1][i] && is_space(av[1][i]) == 1)
		i++;
	while (is_space(av[1][i]) == 0 && av[1][i])
	{
		write(1, &av[1][i++], 1);
	}
	return (write(1, "\n", 1), 0);
}
