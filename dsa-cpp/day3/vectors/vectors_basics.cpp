#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector <int> nums={10,20,30,40};

	for(int i=0;i<nums.size();i++)
	{
		cout<<nums[i]<<endl;
	}

	vector <int> nums2={};
	int x,y;
	cout<<"Enter the no. of elements : ";
	cin>>x;
	for(int i=0;i<x;i++)
	{
		cout<<"Enter the element :";
		cin>>y;
		nums2.push_back(y);
	}
	for(int i=0;i<nums2.size();i++)
	{
		cout<<nums2[i]<<endl;
	}
	nums2.pop_back();
	for(int i=0;i<nums2.size();i++)
	{
		cout<<nums2[i]<<endl;
	}

}