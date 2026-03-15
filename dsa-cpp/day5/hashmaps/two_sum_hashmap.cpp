#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main()
{
	vector <int> nums={2,7,11,15};
	int target = 9;
	int complement;
	unordered_map <int,int> two_sum;
	for(int i=0;i<nums.size();i++)
	{
		complement=target-nums[i];
		if(two_sum.find(complement)!=two_sum.end())
		{
			cout<<two_sum[complement]<<" "<<i<<endl;
			return 0;
		}
		two_sum[nums[i]]=i;
	}
	return 0;
}