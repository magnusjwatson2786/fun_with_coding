#include<stdio.h>
int main()
{
        float r,area;
        printf("Enter the radius of the circle(in cm):\n");
        scanf("%f", &r);
        const float pi=3.14;
        area=pi*r*r;
        printf("Area of the circle is: %f sq.cm\n",area);
        return 0;
}
