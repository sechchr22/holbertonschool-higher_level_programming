#include "lists.h"
/**
* check_cycle - function to check if there is a cycle in a linked list
* @list: pointer to head of the linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	struct listint_s *p1, *p2;

	p1 = list;
	p2 = p1->next;

	if (list == NULL || list->next == NULL || list->next->next == NULL)
	return (0);

	while (p2->next != NULL)
	{
		if (p1 == p2)
		return (1);

		p2 = p2->next;
		p2 = p2->next;
		p1 = p1->next;
	}

return(0);
}
