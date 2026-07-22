/* paramsum */
/* Fonctions autorisees : write */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putnbr(int nb)
{
	long	n = nb;
	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	if (n >= 10)
		ft_putnbr(n / 10);
	ft_putchar(n % 10 + '0');
}
int	main(int ac, char **av)
{
	(void)av;
	if (ac < 2)
		return (write(1, "0\n", 2), 0);
	ft_putnbr(ac - 1);
	return (write(1, "\n", 1), 0);
}
