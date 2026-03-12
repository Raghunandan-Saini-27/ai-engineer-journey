#include<iostream>
#include<vector>
using namespace std;

int main()
{
	vector <int> nums={1,2,3,4};
	bool x=false;
	for(int i=0;i<nums.size();i++)
	{
		int duplicate=nums[i];
		for(int j=i+1;j<nums.size();j++)
		{
			if(duplicate==nums[j])
			{
				x=true;
				break;
			}
		}
		if(x==true)
		{
			break;
		}
	}
	cout << boolalpha << x;
	return 0;
}