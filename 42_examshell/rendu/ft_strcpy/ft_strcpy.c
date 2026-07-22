/* ft_strcpy */

char    *ft_strcpy(char *dst, char *src)
{
	int	i = 0;
	while (src[i])
	{
		dst[i] = src[i];
		i++;
	}
	return (dst);
}
