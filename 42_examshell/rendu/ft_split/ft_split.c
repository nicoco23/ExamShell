/* ft_split */
/* Fonctions autorisees : malloc */

#include <stdlib.h>

int	is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

static int	count_words(char *s)
{
	int	count = 0;
	int	in_word = 0;

	while (*s)
	{
		if (!is_space(*s) && !in_word)
		{
			in_word = 1;
			count++;
		}
		else if (is_space(*s))
			in_word = 0;
		s++;
	}
	return (count);
}

char	*extract_word(char *s, int *i)
{
	int		start = *i;
	char	*word;
	int		len;

	while (s[*i] && !is_space(s[*i]))
		(*i)++;
	len = *i - start;
	word = malloc(sizeof(char) * (len + 1));
	if (!word)
		return NULL;
	len = 0;
	while (start + len < *i)
	{
		word[len] = s[start + len];
		len++;
	}
	word[len] = '\0';
	return (word);
}

void	free_split(char **split, int n)
{
	while (n > 0)
		free(split[--n]);
	free(split);
}

char    **ft_split(char *str)
{
	char	**result;
	int		nwords;
	int		i = 0;
	int		w = 0;

	nwords = count_words(str);
	result = malloc(sizeof(char *) * (nwords + 1));
	if (!result)
		return NULL;
	while (w < nwords)
	{
		while (is_space(str[i]))
			i++;
		result[w] = extract_word(str, &i);
		if (!result[w])
		{
			free_split(result, w);
			return NULL;
		}
		w++;
	}
	result[w] = NULL;
	return (result);
}
