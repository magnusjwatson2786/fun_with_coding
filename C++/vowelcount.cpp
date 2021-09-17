#include <string>
#include <iostream>

using namespace std;

int getCount(const string& inputStr){
  int num_vowels = 0;
  for (auto p: inputStr){
    if (p=='a')
        num_vowels+=1;
    if (p=='e')
        num_vowels+=1;
    if (p=='i')
        num_vowels+=1;
    if (p=='o')
        num_vowels+=1;
    if (p=='u')
        num_vowels+=1;
  }
  //your code here
  return num_vowels;
}
int main(){
    std::cout<<getCount("abracadabra");

return 0;}
