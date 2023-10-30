#include"lists.h"
#include<stdio.h>
#include<stdlib.h>

/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: Pointer to the head of the list
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *runner1 = list;
	listint_t *runner2 = list;

	while (runner1 && runner1->next)
	{
		runner1 = runner1->next->next;
		runner2 = runner2->next;
		if (runner1 == runner2)
		{
			return (1);
		}

	}
	return (0);
}
