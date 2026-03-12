#include<iostream>
#include<vector>
using namespace std;

int main()
{
	vector <int> nums={1,2,3,4,5};
	int n=nums.size();
	for(int i=0;i<nums.size()/2;i++)
	{
		swap(nums[i],nums[n-i-1]);
	}
	for(int i=0;i<nums.size();i++)
	{
		cout<<nums[i]<<endl;
	}
}