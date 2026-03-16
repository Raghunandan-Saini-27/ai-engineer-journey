#include <iostream> 
#include <set>
using namespace std;

int main()
{
	set <int> nums;
	nums.insert(10);
	nums.insert(20);
	nums.insert(20);
	nums.insert(30);
	for(int i : nums)
	{
		cout<<i<<" ";
	}
}