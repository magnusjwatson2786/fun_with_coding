#include<stdio.h>
#include<stdlib.h>
/*Function declaration*/
int isEven(const int NUM);
int main()
{
        int num;
        FILE *fptrOdd, *fptrEven;
        fptrOdd=fopen("odd.txt","w");
        fptrEven=fopen("even.txt","w");
        if(fptrOdd==NULL || fptrEven==NULL)
{
        printf("Error! Can't write into the file.\n");
        exit(1);
}
        printf("File successfully created! :D\n");
        printf("Enter number: \n");
        scanf("%d", &num);
{
        if (isEven(num))
                fprintf(fptrEven, "%d\n", num);
        else
                fprintf(fptrOdd, "%d\n", num);
}
        fclose(fptrOdd);
        fclose(fptrEven);
        printf("Odd and Even numbers are successfully written in the file. :D\n"
);
        return 0;
}
int isEven(const int NUM)
{
  return !(NUM & 1);
}
