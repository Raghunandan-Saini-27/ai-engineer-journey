#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector <int> nums={1,2,5,1,7,1,1};
	int k = 3;							//Target-Sum
	int sum=0;
	int left=0;
	int max_length=0;
	for(int right=0;right<nums.size();right++)
	{
		sum=sum+nums[right];
		if(sum>=k)
		{
			while(sum>k)
			{	
				sum=sum-nums[left];
				left++;
			}
			if(sum==k)
			{
				max_length=max(max_length,right-left+1);
			}
		}
	}
	cout<<max_length;
}