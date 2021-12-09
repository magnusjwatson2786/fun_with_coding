#include<stdio.h>
int main()
{
        float num;
        printf("Enter the number: \n");
        scanf("%f", &num);
        if ((int)num%2==0)
                printf("The number entered is even\n");
        else
                printf("The number entered is odd\n");
        return 0;
}
