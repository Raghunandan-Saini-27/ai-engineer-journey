#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int arr[] = {2,1,5,1,3,2};
	int k = 3;
	int x=sizeof(arr)/sizeof(arr[0]);
	int sum_window=0;
	int max_val=arr[0];
	for(int i=0;i<k;i++)
	{
		sum_window+=arr[i];
	}
	
	for(int i=0;i<x-k;i++)
	{
		sum_window=sum_window+arr[i+k]-arr[i];
		cout<<sum_window<<endl;
		if(sum_window>max_val)
		{
			max_val=sum_window;
		}
	}
	cout<<"max sum of subarray is : "<<max_val<<endl;
}