#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the linked list
 * Return: if linked list has a cycle or not
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;

	fast = list;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	while (fast->next != NULL && fast->next->next != NULL)
	{
		fast = fast->next;
		fast = fast->next->next;
		if (list == fast)
			return (1);
	}
	return (0);
}
