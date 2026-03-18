# include <iostream>
# include <string>
# include <set>
using namespace std;

int main()
{
	string str="abcabcbb";
	set <char> s;
	int left=0,max_length=0;
	for(int right=0;right<str.length();right++)
	{
		while(s.count(str[right]))
		{
			s.erase(str[left]);
			left++;
		}
		s.insert(str[right]);
		max_length=max(max_length,right-left+1);
	}
	cout<<max_length<<endl;
	
}