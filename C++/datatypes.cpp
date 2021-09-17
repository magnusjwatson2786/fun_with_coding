#include <iostream>
#include <string>
// using namespace std;

int main() {
    
    int number;
    std::string name = "Mike";    // string of characters, not primitive
    char testGrade = 'A';    // single 8-bit character.

    // you can make them unsigned by adding "unsigned" prefix
    short age0 = 10;         // atleast 16-bits signed integer
    int age1 = 20;           // atleast 16-bits signed integer (not smaller than short)
    long age2 = 30;          // atleast 32-bits signed integer
    long long age3 = 40;     // atleast 64-bits signed integer

    float gpa0 = 2.5f;       // single percision floating point
    double gpa1 = 3.5;       // double-precision floating point
    long double gpa2 = 3.5;  // extended-precision floating point

    int nums[]= {1,2,3,4,5,5,5,7};
    std::cout<< sizeof(nums) <<std::endl;

    bool isTall;             // 1 bit -> true/false
    isTall = true;

    name = "John";

    std::cout << "Your name is " << name << std::endl;

    std::cout << "hello world!" << std::endl;
    std::cout << "enter a number: ";
    std::cin >> number;
    std::cin.ignore(); // removes the newline char from cin input buffer
    std::cout << "You entered :" << number << std::endl ;

    std::cout << "Enter your name : ";// << std::endl;
    std::getline(std::cin, name); // required for multiword string since breaks off at whitespaces
    std::cout << "your name is " << name <<std::endl;
    
    std::string greeting = "Hello";
    std::cout << greeting[0] << std::endl;
    std::cout << greeting.length() << std::endl;
    std::cout << greeting.find("llo") << std::endl;
    std::cout << greeting.substr(2) << std::endl;
    std::cout << greeting.substr(1, 3) << std::endl;


    return 0;
}