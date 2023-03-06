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
	listint_t *fast, *slow;

	fast = slow = list;

	if(list == NULL)
		return (false);

	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (false);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (true);
}
