/* ft_split */
/* Fonctions autorisees : malloc */

#include <stdlib.h>


char    **ft_split(char *str)
{
	char	**phrase;
	int		i = 0;
	int		word = 0;
	int		j = 0;

	while (str[i])
	{
		while (str[i] != 32 || (str[i] > 13))
		{
			phrase[word][j] = str[i];
			i++;
		}
	word++;
	j = 0;
	i++;
	} 
}
