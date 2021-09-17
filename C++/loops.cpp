#include <iostream>
#include <string>
#include <time.h>

void forloop(int x[]);

int main(){

    srand(time(0));
    std::cout<< time(0) <<std::endl;
    int i, guess, guesscount=0, guesslimit=3;
    i = (rand()%10)+1; 
    while (true){
        if(guesscount==guesslimit){
            std::cout<< "\nYou ran out of guesses! PEPOSADGE";
            break;
        }
        std::cout<< "\nEnter your guess : ";
        std::cin >> guess;
        if (guess==i){
            std::cout<< "\nYou Guessed it!";
            break;
        }
        if (guess>i){
            std::cout<< "Too high!";
        }
        else if (guess<i){
            std::cout<< "Too low!";
        }
        std::cin.ignore();
        guesscount++;
    }
    
    std::cout<< "\nYou can rest for now, Soldier.\n";

    // int nums[]= {1,2,3,4,5,5,5,7};
    forloop(20);

    return 0;
}

void forloop(int x){
    for(int i=0; i<x; i++){
        std::cout<<i;
    }
}
