#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main()
{
	int nums1[] = {1,2,2,3}, nums2[] = {2,3,4};
	int size=sizeof(nums1)/sizeof(nums1[0]);
	vector <int> result{};
	set <int> s1(nums1,nums1+size);
	for(int x:nums2)
	{
		if(s1.count(x))
		{
			result.push_back(x);
			s1.erase(x);
		}
	}
	for(int y:result)
	{
		cout<<y<<endl;
	}
}