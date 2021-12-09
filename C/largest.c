#include<stdio.h>
int main()
{
        int num1,num2,num3;
        printf("Enter three different numbers:- \n");
        printf("First number: \n");
        scanf("%d", &num1);
        printf("Second number: \n");
        scanf("%d", &num2);
        printf("Third number: \n");
        scanf("%d", &num3);
        if (num1 >= num2 && num1 >= num3)
                printf("\n%d is the largest number\n",num1);
        else if (num2 >= num1 && num2 >=num3)
                printf("\n%d is the largest number\n",num2);
        else
                printf("\n%d is the largest number\n",num3);
        return 0;
}
