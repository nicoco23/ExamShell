/* search_and_replace */
/* Fonctions autorisees : write, exit */

#include <unistd.h>
#include <stdlib.h>

int	main(int ac, char **av)
{
	if (ac != 4)
		return (write(1, "\n", 1), 0);
	char	rep = av[2];
	return (0);
}
