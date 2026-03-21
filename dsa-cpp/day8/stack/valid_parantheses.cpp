#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool valid_parantheses()
{
	string str="()[]{}";
	stack <char> s;
	for(int i=0;i<str.length();i++)
	{
		if(str[i]=='{' || str[i]=='[' || str[i]=='(')
		{
		s.push(str[i]);
		}

		else
		{
			if(s.empty())
			{
				return false;
			}
			if((str[i]==')' && s.top()=='(') || (str[i]=='}' && s.top()=='{') || str[i]==']' && s.top()=='[')
			{
				s.pop();
			}
			else
			{
				return false;
			}
		}
	}
	return s.empty();
}

int main()
{
	bool x=valid_parantheses();
	cout<<boolalpha<<x;
}