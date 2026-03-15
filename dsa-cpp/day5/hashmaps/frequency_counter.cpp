#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main()
{
	unordered_map <int,int> freq_count;
	vector <int> num={1,2,2,3,3,3};
	for(int i=0;i<num.size();i++)
	{
		freq_count[num[i]]++;
	}

	for(auto const& x:freq_count)
	{
	cout<<x.first<<" : "<<x.second<<endl;
	}
}