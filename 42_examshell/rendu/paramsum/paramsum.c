/* paramsum */
/* Fonctions autorisees : write */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putnbr(int nb)
{
	if (nb >= 10)
		ft_putnbr(nb / 10);
	ft_putchar(nb % 10 + '0');
}

int	main(int ac, char **argv)
{
	(void)argv;
	if (ac < 2)
		return (write(1, "0\n", 2), 0);
	ft_putnbr(ac - 1);
	return (write(1, "\n", 1), 0);
}
