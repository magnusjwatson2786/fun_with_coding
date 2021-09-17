#include <iostream>
#include <string>
#include <cmath>

float calc(float number1, float number2, char operation);
std::string getWeekDay(int dayNum); //prototypes

int main(){
    int a=3,b=4,c=5;
    std::cout<< fmax(c,fmax(a,b)) <<std::endl;
    std::cout<< calc(a,b,'a') <<std::endl;
    std::cout<< calc(a,b,'S') <<std::endl;
    std::cout<< calc(a,b,'m') <<std::endl;
    std::cout<< calc(a,b,'D') <<std::endl;
    std::cout<< getWeekDay(0) <<std::endl;
    std::cout<< getWeekDay(1) <<std::endl;
    std::cout<< getWeekDay(2) <<std::endl;
    std::cout<< getWeekDay(3) <<std::endl;
    std::cout<< getWeekDay(4) <<std::endl;
    std::cout<< getWeekDay(5) <<std::endl;
    std::cout<< getWeekDay(6) <<std::endl;
    std::cout<< getWeekDay(7) <<std::endl;
    return 0;
}

float calc(float number1, float number2, char operation){
    if (operation =='A' || operation =='a'){
        return number1+number2;
    }
    if (operation =='S' || operation =='s'){
        return number1-number2;
    }
    if (operation =='M' || operation =='m'){
        return number1*number2;
    }
    if (operation =='D' || operation =='d'){
        return number1/number2;
    }
    else {
        return -1;
    }
}

std::string getWeekDay(int dayNum){
    std::string dayName;

    switch (dayNum)
    {
    case 1:
        dayName="Sunday";
        break;
    case 2:
        dayName="Monday";
        break;
    case 3:
        dayName="Tuesday";
        break;
    case 4:
        dayName="Wednesday";
        break;
    case 5:
        dayName="Thursday";
        break;
    case 6:
        dayName="Friday";
        break;
    case 7:
        dayName="Saturday";
        break;
    default:
        dayName="Invalid day no.";
        break;
    }

    return dayName;
}