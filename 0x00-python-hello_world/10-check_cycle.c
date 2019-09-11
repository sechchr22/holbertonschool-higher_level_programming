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

	while (1)
	{
		if (p1 == p2)
		return (1);

		else if (p2->next == NULL)
		return (0);

		p2 = p2->next;
		p2 = p2->next;
		p1 = p1->next;
	}
}