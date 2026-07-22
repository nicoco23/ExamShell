/* ft_strdup */
/* Fonctions autorisees : malloc */

#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i = 0;
	while(str[i])
		i++;
	return (i);
}

char    *ft_strdup(char *src)
{
	size_t	len = ft_strlen(src);
	char	*dup = malloc(len + 1);
	if (!dup)
		return NULL;
	size_t	i = 0;
	while(src[i])
	{
		dup[i] = src[i];
		i++;
	}
	dup[i] = '\0';
	return dup;
}
