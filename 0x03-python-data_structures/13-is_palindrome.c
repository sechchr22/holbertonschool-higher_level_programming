#include "lists.h"

/**
 * list_len - function that returns the number
 * of elements in a linked list_t list.
 * @h: pointer to a node
 * Return: number of nodes
*/

size_t list_len(const list_t *h)
{
	unsigned int count = 0;

	while (h != NULL)
	{
		h = h->next;
		count = count + 1;
	}

return (count);
}

/**
 * is_palindrome - function to determine if a linked list
 * is a palindrome
 * @head: double pointer holding pointer head of list
 * Return: 1 if it is palindrome, 0 if not
*/

int is_palindrome(listint_t **head)
{
	size_t sum1 = 0, sum2 = 0, i, j;
	size_t half1 = 0, half2 = 0;

	listint_t *temp = *head;

	if (*head == NULL)
	return (0);
	else if ((*head)->next == NULL)
	return (1);

	if (list_len(temp) % 2 == 0)
	{
		half2 = (list_len(temp) / 2);
		half1 = half2 - 1;

		for (i = 0, i <= half1, i++)
		{
			sum1 = sum1 + temp->n;
			temp = temp->next;
		}
		temp = temp->next;
		i++;
		for (j = i; j < list_len(temp); j++)
		{
			sum2 = sum2 + temp->n;
			temp = temp->next;
		}
		if (sum1 == suma2)
		return (1);
		else
		return (0);
	}
}
