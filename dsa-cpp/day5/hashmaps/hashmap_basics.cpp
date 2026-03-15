#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
	unordered_map <string,int> fruits;
	fruits["apple"]=5;
	fruits["banana"]=12;
	fruits["mango"]=2;

	for(auto item:fruits)
	{
		cout<<item.first<<" "<<item.second<<endl;
	}
}