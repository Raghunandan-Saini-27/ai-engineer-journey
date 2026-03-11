#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector <int> nums={-2,1,-3,4,-1,2,1,-5,4};
	int max_so_far=nums[0];
	int i,j;
	for(i=0;i<nums.size();i++)
	{
		int current_sum=0;
		for(j=i;j<nums.size();j++)
		{
			current_sum+=nums[j];
			if(current_sum>max_so_far)
			{
				max_so_far=current_sum;
			}
		}
	}
	cout<<"max sum :"<<max_so_far; 
}
