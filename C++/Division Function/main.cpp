#include <iostream>
#include <conio.h>
#include <math.h>
#include <iomanip>

using namespace std;

float div(int y,int x)
{
    //x divides y
    int q1,q2,q3,r,r1,r2;
    float z;

    q1=y/x;
    r=y%x;
    z=q1;

    if(r!=0)
    {
        q2=(r*10)/x;
        r1=(r*10)%x;
        z=((q1*10)+q2)*pow(10,-1);
    }
    if(r1!=0)
    {
        q3=(r1*10)/x;
        r2=(r1*10)%x;
        z=((q1*100)+(q2*10)+q3)*pow(10,-2);
    }
    return z;
}

int main()
{
    int x,y;
    cout << "Hello world!" << endl;
    cout<< "1st";
    cin>>x;
    cout<< "2nd";
    cin>>y;
    cout<<"\nlets check :"<<div(x,y);
    getch();
    return 0;
}
