#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: A pointer to a pointer to the head of the linked list.
 * @number: The integer value to be inserted into the list.
 *
 * Return: The address of the new node, or NULL if it fails to insert.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *ptr_now = *head;

	if (!new)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (!ptr_now || new->n < ptr_now->n)
	{
		new->next = ptr_now;
		return (*head = new);
	}
	while (ptr_now)
	{
		if (!ptr_now->next || new->n < ptr_now->next->n)
		{
			new->next = ptr_now->next;
			ptr_now->next = new;
			return (ptr_now);
		}
		ptr_now = ptr_now->next;
	}
	return (NULL);
}
