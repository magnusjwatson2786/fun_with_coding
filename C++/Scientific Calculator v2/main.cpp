#include <iostream>
#include <conio.h>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    int choice;
    char continu='y';
    cout << "\nHello User!";
    cout << "\n           SCIENTIFIC CALCULATOR!             ";
    while (continu!='n'){
    cout <<"\nPress 1 for addition";
    cout <<"\nPress 2 for Subtraction";
    cout <<"\nPress 3 for Multiplication";
    cout <<"\nPress 4 for Division";
    cout <<"\nPress 5 for Absolute Value";
    cout <<"\nPress 6 for Exponential Multiplication";
    cout <<"\nPress 7 for square root";
    cout <<"\nPress 8 for sine";
    cout <<"\nPress 9 for cosine";
    cout <<"\nPress 10 for tangent";
    cout <<"\nPress 11 for cosecant";
    cout <<"\nPress 12 for secant";
    cout <<"\nPress 13 for cotangent";
    cout <<"\nPress 14 for log(base e)";
    cout <<"\nPress 15 for log(base 10)";
    cout <<"\nEnter Your Choice:";
    cin>>choice;
    switch(choice)
    {
        case 1 :
            {
                char response='y';
                while (response!='n'){
                float x,y;
                cout<<"\nEnter 1st no:";
             cin>>x;
             cout<<"\nEnter 2nd no:";
             cin>>y;
             cout<<"\nsum="<<x+y;
             cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Additions?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 2 :
            {
                char response='y';
                while (response!='n'){
                float x,y;
                cout<<"\nEnter 1st no:";
             cin>>x;
             cout<<"\nEnter 2nd no:";
             cin>>y;
             cout<<"\nDifference="<<x-y;
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Subtraction?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 3 :
            {
                char response='y';
                while (response!='n'){
                float x,y;
                cout<<"\nEnter 1st no:";
             cin>>x;
             cout<<"\nEnter 2nd no:";
             cin>>y;
             cout<<"\nProduct="<<x*y;
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Multiplication?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 4 :
            {
                char response='y';
                while (response!='n'){
                int x,y;
                cout<<"\nEnter Dividend:";
             cin>>x;
             cout<<"\nEnter Divisor:";
             cin>>y;
             cout<<"\nQuotient="<<(x/y)<<" Remainder="<<(x%y);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Division?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 5 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the decimal no:";
                cin>>x;
                cout<<"\nAbsolute value="<<fabs(x);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more like these?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 6 :
            {
                char response='y';
                while (response!='n'){
                double x,y;
                cout<<"\nEnter base no:";
             cin>>x;
             cout<<"\nEnter exponent:";
             cin>>y;
             cout<<"\nResult="<<pow(x,y);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Exponential Multiplications?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 7 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the no:";
                cin>>x;
                cout<<"\nSquare Root="<<sqrt(x);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Square roots?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 8 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the angle(in radians):";
                cin>>x;
                cout<<"\nRequired Sine Value="<<sin(x);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more like these?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 9 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the angle(in radians):";
                cin>>x;
                cout<<"\nRequired Cosine Value="<<cos(x);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more like these?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 10 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the angle(in radians):";
                cin>>x;
                cout<<"\nRequired Tangent Value="<<tan(x);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more like these?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 11 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the angle(in radians):";
                cin>>x;
                cout<<"\nApprox Cosecant Value="<<1/(sin(x));
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more like these?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 12 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the angle(in radians):";
                cin>>x;
                cout<<"\nApprox secant Value="<<1/(cos(x));
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more like these?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 13 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the angle(in radians):";
                cin>>x;
                cout<<"\nApprox Cotangent Value="<<1/(tan(x));
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more like these?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 14 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the no.:";
                cin>>x;
                cout<<"\nNatural Logarithm="<<log(x);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Log values?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        case 15 :
            {
                char response='y';
                while (response!='n'){
                double x;
                cout<<"\nEnter the no.:";
                cin>>x;
                cout<<"\nLogarithm to base 10="<<log10(x);
            cout<<"\nPress enter to continue";
            getch();
            cout<<"\nDo you want more Log values?[y/n]";
        cin>>response;
        if (response=='y'){cout<<"\nlets start again";}
        else{break;}}
        break;}
        default:
            {
                cout<<"\nInvalid Value";
                break;
            }
    }
    cout<<"\nDo you want to use other Calculations?[y/n]";
    cin>>continu;
    if (continu=='y'){cout<<"\nLets start again";}
        else{cout<<"\n      USE ME WHEN YOU NEED\n";
            break;
            getch();}
    }
    return 0;
}
