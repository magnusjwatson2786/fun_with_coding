/*Developing this subtraction program to perform on integer values */
 
#include<stdio.h>
int main()
{
        int num1, num2, output;
        printf("This program is meant for subtracting two number\n");
        printf("Enter the first number: \n"), scanf("%d",&num1);
        printf("Enter the second number: \n");
        scanf("%d",&num2);
        output=num1-num2;
        printf("Subtraction of two numbers %d and %d is: %d\n",num1,num2,output);
        return 0;
}
