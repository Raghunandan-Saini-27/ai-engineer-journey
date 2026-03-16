#include<iostream>
#include<vector>
#include<set>
using namespace std;

int main()
{
	vector <int> v={1,2,2,3,3,4,5};
	set <int> s (v.begin(),v.end());
	v.assign(s.begin(),s.end());
	for(int x:s)
	{
		cout<<x<<" ";
	}
	return 0;
}