#include <iostream>

unsigned int countBits(unsigned long long n);
int main(){

    std::cout<<countBits(4);
    return 0;
}

unsigned int countBits(unsigned long long n){
  unsigned int c=0;
  while(n){
    c+=n&1;
    n>>=1;}
  return c;
}
