#include <stdlib.h>
#include "ft_list.h"

int cmp(void *a, void *b);

void ft_list_remove_if(t_list **begin, void *data, int (*cmp)(void *, void *))
{
	if (begin == NULL || *begin == NULL)
		return;

	t_list *cur = *begin;

	if (cmp(cur->data, data) == 0)
	{
		*begin = cur->next;
		free(cur);
		ft_list_remove_if(begin, data, cmp);
	}
	else
		ft_list_remove_if(&cur->next, data, cmp);
}