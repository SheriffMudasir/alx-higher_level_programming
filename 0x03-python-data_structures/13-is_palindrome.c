#include <stdio.h>
#include "lists.h"

/**
 * reverseList - This function reverse the list
 * @head: pointer to pointer of first node of listint_t list
 * Return: the reversed list
 */
void reverseList(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - This function checks if a list is a palindrone
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	listint_t *current;
	listint_t *reversedHead;

	current = *head;
	reversedHead = NULL;

	reverseList(&current);
	reversedHead = current;

	while (*head != NULL && reversedHead != NULL)
	{
		if ((*head)->n != reversedHead->n)
		{
			return (0);
		}
		*head = (*head)->next;
		reversedHead = reversedHead->next;
	}
	return (1);
}
