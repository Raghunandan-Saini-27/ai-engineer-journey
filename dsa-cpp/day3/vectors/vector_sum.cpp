#include<iostream>
#include<vector>
using namespace std;

int main()
{
	vector <int> nums={2,4,6,8};
	int sum=0;
	for(int i=0;i<nums.size();i++)
	{
		sum+=nums[i];
	}
	cout<<"Sum of elements : "<<sum<<endl;
}