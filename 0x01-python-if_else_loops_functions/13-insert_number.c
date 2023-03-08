#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - function that inserts number into a SSLL
 * @head: input pointer to head pointer of singly linked list
 * @number: input number to sort and insert into list as new node
 * Return: address of newly adde node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t)),	*first, *second;

	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	if (head == NULL)
		head = &newNode;
		return (newNode);
	if (*head == NULL)
		(*head) == newNode;
		return (newNode);
	if ((*head)->n >= number)
		newNode->next = (*head);
		(*head) = newNode;
		return (newNode);
	first = second = *head;
	while (second->n != NULL && second->next->next != NULL)
	{
		second = second->next->next;
		if (second->n < number)
			first = second;
		else if (first->next->n <= number)
			newNode->next = first->next->next;
			first->next->next = newNode;
			return (newNode);
		else if (first->n <= number)
			newNode->next = first->next;
			first->next = newNode;
			return (newNode);
	}
	if (second->next == NULL)
		second->next = newNode;
		return (newNode);
	if (second->next->n <= number)
		second->next->next = newNode;
		return (newNode);
	newNode->next = second->next;
	second->next = newNode;
	return (newNode);
}
