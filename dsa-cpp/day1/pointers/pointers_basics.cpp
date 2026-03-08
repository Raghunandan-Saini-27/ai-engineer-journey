# include <iostream>
using namespace std;

void pt();

int main()
{
	int num=10;
	int *ptr=&num;

	cout<<"Value of num : "<<num<<endl;
	cout<<"Adress of num : "<<&num<<endl;

	cout<<"ptr stores : "<<ptr<<endl;
	cout<<"Value using pointer : "<<*ptr<<endl;

	*ptr=20;
	cout<<"Value using pointer : "<<*ptr<<endl;

	pt();

}

void pt()
{
	int number;
	cout<<"Enter the number : ";
	cin>>number;

	int *y=&number;
	cout<<"Square of number using pointer : "<<(*y)*(*y)<<endl;
	cout<<"ptr stores value : "<<*y<<endl;
	cout<<"ptr stores adress: "<<y<<endl;
	
}