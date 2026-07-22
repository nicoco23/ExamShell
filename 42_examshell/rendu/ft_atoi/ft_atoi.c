/* ft_atoi */
/* Fonctions autorisees : None */

int	ft_atoi(const char *str)
{
	int	i = 0;
	int	sign = 1;
	int	res = 0;

	while (str[i] == 32 || (str[i] >= 7 && str[i] <= 13))
		i++;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			sign = -sign;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		res = res * 10 + (str[i] - '0');
		i++;
	}
	return (res * sign);
}
