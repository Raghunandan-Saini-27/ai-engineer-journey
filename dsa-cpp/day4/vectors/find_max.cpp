#include<iostream>
#include<vector>
using namespace std;

int main()
{
	vector <int> nums={12,45,2,67,34};
	int max_val=nums[0];
	for(int i=0;i<nums.size();i++)
	{
		if(nums[i]>max_val)
		{
			max_val=nums[i];
		}
	}
	cout<<max_val;
}