#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector <int> nums= {1,4,2,10,2,3,1};
	int k = 3;
	int max_sum=0;
	int max_val=0;
	for(int i=0;i<k;i++)
	{
		max_sum+=nums[i];
	}
	cout<<max_sum<<endl;
	for(int i=0;i<nums.size()-k;i++)
	{
		max_sum=max_sum+nums[i+k]-nums[i];
		if(max_sum>max_val)
		{
			max_val=max_sum;
		}
	}
	cout<<max_val;
}