#include<iostream>
using std::cout;
using std::cin;
using std::endl;

int main(int argc, char const *argv[])
{
	int k;
	cin>> k;
	if (k==2)
		cout<<"NO";
	else
		k%2?cout<<"NO":cout<<"YES";
	return 0;
}