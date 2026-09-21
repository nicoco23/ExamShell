/* print_hex */
/* Fonctions autorisees : write */
#include <unistd.h>

int	atoi(char *str)
{
	int	i = 0;
	int	sign = 1;
	int	res = 0;

	while (str[i] == 32 || (str[i] >= 9 && str[i] <= 13))
		i++;
	while (str[i] == '+' || str[i] == '-')
		if (str[i++] == '-')
			sign = -sign;
	while (str[i] >= '0' && str[i] <= '9')
	{
		res = res * 10 + (str[i] - '0');
		i++;
	}
	return (res);
}

void	ft_putnbr(int nb)
{
	long	n = nb;
	
}

int	main(int ac, char **av)
{
	if (ac != 2)
		return (write(1, "\n", 1), 0);
	
	return (0);
}
