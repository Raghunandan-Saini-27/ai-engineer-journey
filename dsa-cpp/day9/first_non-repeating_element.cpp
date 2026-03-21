#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int sol()
{
	vector <int> v={2,3,4,2,3,5};
	unordered_map <int,int> m;
	queue <int> q;
	for(int i=0;i<v.size();i++)
	{
		int current=v[i];
		m[current]++;
		q.push(i);
	}
	while(!q.empty())
	{
		if(m[(q.front())]>1)
		{
			q.pop();
		}
		else
		{
			return q.front();
		}
		
	}
	return -1;
}

int main()
{
	int x=sol();
	cout<<x;
	return 0;
}