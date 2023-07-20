/*arranging ins ascending order using bubble sort*/

#include <stdio.h>
#define MAX 5

/**
* main - entry point
* Return: always zero
*/

int main(void)
{
	int i = 0;
	int temp;
	int j = 0;
	int my_number[MAX] = {40, 17, 9, 15, 50};

	for (; i < MAX - 1; i++)
	{
		for (; j < MAX - 1; j++)
		{
			if (my_number[j] > my_number[j + 1])
			{
				temp = my_number[j];
				my_number[j] = my_number[j + 1];
				my_number[j + 1] = temp;
			}
		}
		printf("%d", my_number[i + 1]);
		printf(", ");
	}
	printf("\n");
}
