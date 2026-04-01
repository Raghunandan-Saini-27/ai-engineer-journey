#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main()
{
	vector <int> nums={1,3,-1,-3,5,3,6,7};
	int k=3;
	deque <int> dq;
	vector <int> result;
	for(int i=0;i<nums.size();i++)
	{
		if (!dq.empty() && dq.front() == i - k) {
            dq.pop_front();
        }
		while (!dq.empty() && nums[i] >= nums[dq.back()]) {
            dq.pop_back();
        }
		dq.push_back(i);
		if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
	}

	for (int x : result)
	{
		cout << x << " ";
	}
	
	return 0;
}