#include<iostream>
#include<vector>
using namespace std;

int max_sum_subarr()
{
	vector <int> nums={2,1,5,1,3,2};
	int k=3;
	int max_sum=nums[0];
	int win_sum=0;
	for(int i=0;i<k;i++)
	{
		win_sum+=nums[i];
	}
	for(int i=0;i<nums.size()-k;i++)
	{
		win_sum=win_sum+nums[i+k]-nums[i];
		if (win_sum>=max_sum)
		{
			max_sum=win_sum;
		}
		
	}
	return max_sum;
}

int main()
{
	int x;
	x=max_sum_subarr();
	cout<<"Max Sum :"<<x<<endl;
}