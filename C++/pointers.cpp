#include <iostream>
#include <string>

int main(){ 

    int age=19;
    double gpa = 2.7;
    std::string name="Mike";

    std::cout<< &age <<std::endl; // prints memory addresses (pointers)
    std::cout<< &gpa <<std::endl;
    std::cout<< &name <<std::endl;

    std::cout<< *&age <<std::endl; // dereferences the memory addresses back to the values
    std::cout<< *&gpa <<std::endl;
    std::cout<< *&name <<std::endl;

    int *page= &age;         // creates pointer variables
    double *pgpa = &gpa;
    std::string *pname= &name;

    std::cout<< page <<std::endl; // prints the pointers in the pointer variables
    std::cout<< pgpa <<std::endl;
    std::cout<< pname <<std::endl;

    std::cout<< *page <<std::endl; // dereferences the pointers in the pointer variables
    std::cout<< *pgpa <<std::endl;
    std::cout<< *pname <<std::endl;

    return 0; 
}

// & points towards the address
// * points towards the value