#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	return (Compare(head, *head));
}

/**
 * Compare - recursively compares the linked list nodes
 * @head: pointer to a pointer to the left node
 * @end: pointer to the right node
 * Return: 1 if it's a palindrome, 0 otherwise
 */

int Compare(listint_t **head, listint_t *end)
{
	if (end == NULL)
	{
		return (1);
	}
	if (Compare(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
