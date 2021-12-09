#include<stdio.h>
#include<stdlib.h>
int main()
{
        int num;
        FILE *fptr;
        if ((fptr = fopen("numbers.txt","r")) == NULL)
{
        printf("Error! File cannot be found/opened\n");
        exit(1);
}
        fscanf(fptr," %d", &num);
        if (num%2==0)
                printf("The number is even\n");
        else
                printf("The number is odd\n");
        fclose(fptr);
        return 0;
}
