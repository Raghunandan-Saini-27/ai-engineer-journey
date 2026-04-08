#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector<int> nums={1,3,-2,5,-3,7,8,0,1};
	vector<int> prefix={0};
	int k;
	
	for (int i = 0; i < nums.size(); i++) {
        // We use prefix[i] (the current last element) to calculate the next.
        prefix.push_back(prefix[i] + nums[i]);
    }
	
	for(int i=0;i<prefix.size();i++)
	{
		cout<<prefix[i]<<endl;
	}

	int left,right,result;
	cout<<"Left :";
	cin>>left;

	cout<<"Right :";
	cin>>right;

	result=prefix[right+1]-prefix[left];
	cout<<result;
}