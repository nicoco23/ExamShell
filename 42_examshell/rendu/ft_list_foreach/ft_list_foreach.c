/* ft_list_foreach */

typedef struct	s_list
{
	struct s_list	*next;
	void			*data;
}	t_list;

void    ft_list_foreach(t_list *lst, void (*f)(void *))
{
	while (lst)
	{
		f(lst->data);
		lst = lst->next;
	}
}
