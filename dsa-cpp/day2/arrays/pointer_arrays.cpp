#include <iostream>
using namespace std;

int main()
{
	int arr[5]={10,20,30,40,50};
	int *ptr=arr;
	
	for(int i=0;i<5;i++)
	{
		cout<<*(ptr+i)<<endl;
	}
	cout<<*ptr<<endl;
	cout<<*(ptr+1)<<endl;
	cout<<*(ptr+4)<<endl;

	int arr2[5]={1,2,3,4,5};
	int *ptr2=arr2;
	for(int i=0;i<5;i++)
	{
		cout<<*(ptr2+i)*2<<endl;
	}
}