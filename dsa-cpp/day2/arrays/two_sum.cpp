#include <iostream>
using namespace std;

int main()
{
	int nums[4]={2,7,11,15},target = 9;

/*Output:
0 1*/

	int i,j;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;i++)
		{
			if(nums[i]+nums[j]==target)
			{
				cout<<i<<endl;
				cout<<j<<endl;
			}
		}
	}
}