/* ft_putstr */
/* Fonctions autorisees : write */

#include <unistd.h>

int	ft_strlen(char *str)
{
	int	i = 0;
	while (str[i])
		i++;
	return (i);
}

void	ft_putstr(char *str)
{
	int	i = ft_strlen(str);
	write(1, str, i);
}
