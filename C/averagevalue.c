/* Developing a program that calaculates average value */
 
#include<stdio.h>
int main()
{
        float iw1,nop1,iw2,nop2,average;
        printf("Enter the value of weight and no. of items\n");
        printf("Weight of item1 is: \n");
        scanf("%f", &iw1);
        printf("Weight of item2 is: \n");
        scanf("%f", &iw2);
        printf("No. of item1 purchases: \n");
        scanf("%f", &nop1);
        printf("No. of item2 purchases: \n");
        scanf("%f", &nop2);
        average=((iw1*nop1) + (iw2*nop2))/(nop1+nop2);
        printf("Average value= %f\n",average);
        return 0;
}
