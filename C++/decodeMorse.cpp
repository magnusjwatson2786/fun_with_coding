#include <iostream>
#include <string>

std::string decodeMorse(std::string morseCode) {
    std::string decoded;
    std::string remain=morseCode;
    int index;
    std::string x;
    std::string y ="";
    while (remain[0]==' '){         // removing whitespace at the start
        remain=remain.substr(1);
    }
    std::cout<<"done\n";
    while (remain[remain.length()-1]==' '){            // removing whitespace at the end
        remain=remain.substr(0,remain.length()-1);
    }
    std::cout<<"done\n";
    while (remain.find("   ")<remain.length()){
        index=remain.find("   ");
        x = remain.substr(0, index);
        for(char p:x){
            if (p==' '&& y!=""){
                decoded+=y;//tr
                y="";
            }
            else if (p!=' '){
                y+=p;
            }
        }
        decoded+=y;//tr
        y="";
        decoded+=" ";
        remain=remain.substr(index+3);
        std::cout<< x<< "\n";
    }
    for(char p:remain){                 //for the last peice
        if (p==' '){
            decoded+=y;
            y="";
        }
        else{
            y+=p;
        }
    }
    decoded+=y;//tr
    y="";
    std::cout<<decoded;
    std::cout<<"DONE";
}

int main(){

    decodeMorse(".... . .-.. .-.. --- ....... .-- --- .-. .-.. -..");

    return 0;
}

