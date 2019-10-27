#include "sorth.h"

void swap_nodes(listint_t *a, listint_t *b)
{
	listint_t *temp;
	temp = a;

	if (a->prev == NULL && b->next == NULL) /*si el nodo A es la cabeza y el B es el final*/
	{
		a = a->next;
		a->next = NULL;
		b->next = temp
		b->prev = NULL;
		a->prev = head;
	}

	if (a ->prev == NULL) /*si el nodo A es la cabeza y B un nodo normal*/
	{
		a->prev = a->next;
		a->next = b->next;
		b->next->prev = temp;
		a = a->prev;
		b->prev = NULL;
	}

	if (b->next == NULL) /*si el nodo b es el final y A es uno normal*/
	{
		a->prev->next = a->next;
		b->prev = a->prev;
		b->next = temp;
		a->prev = a->next;
		a->next = NULL;
	}

	else
	{
		a->prev->next = a->next;
		b->prev = a->prev;
		a->prev = a->next;
		a->next = b->next;
		b->next->prev = temp;
		b->next = temp;
	}
}
