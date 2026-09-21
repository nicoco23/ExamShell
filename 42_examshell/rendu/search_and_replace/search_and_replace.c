/* search_and_replace */
/* Fonctions autorisees : write, exit */

#include <unistd.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i = 0;
	while (str[i])
		i++;
	return (i);
}

int	main(int ac, char **av)
{
	if (ac != 4 || ft_strlen(av[2]) != 1 || ft_strlen(av[3]) != 1)
		return (write(1, "\n", 1), 0);
	char	*a = av[1];
	char	letter = av[2][0];
	char	replace = av[3][0];
	int		i = 0;

	while (a[i])
	{
		if (a[i] == letter)
			a[i] = replace;
		write(1, &a[i], 1);
		i++;
	}
	return (write(1, "\n", 1), 0);
}
