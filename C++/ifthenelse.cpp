#include <iostream>
#include <string>

void sayHi();

int main(){
    std::cout << "main"<<std::endl;
    sayHi();
    
    bool isStudent = false;
    bool isSmart = false;

    if(isStudent && isSmart){
        std::cout << "You are a student" << std::endl;
    } else if(isStudent && !isSmart){
        std::cout << "You are not a smart student" << std::endl;
    } else {
        std::cout << "You are not a student and not smart" << std::endl;
    }

    // >, <, >=, <=, !=, ==
    if(1 > 3){
        std::cout << "number comparison was true" << std::endl;
    }

    if('a' > 'b'){
        std::cout << "character comparison was true" << std::endl;
    }

    std::string myString = "cat";
    if(myString.compare("cat") != 0){
        std::cout << "string comparison was true" << std::endl;
    }

    return 0;
}

void sayHi(){
  std::cout << "Hello" << std::endl;
}