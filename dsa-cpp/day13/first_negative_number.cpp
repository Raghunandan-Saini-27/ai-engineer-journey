#include<iostream>
#include<vector>
#include<deque>
using namespace std;

int main()
{   
    vector <int> nums={12,-1,-7,8,-15,30,16,28};
    int k=3;
    vector <int> result={};
    deque <int> dq={};
    
    // 1. Process the first window
    for(int i=0;i<k;i++)
    {
        if(nums[i]<0)
        {
            dq.push_back(i);
        }
    }
        
    if(!dq.empty())
    {
        result.push_back(nums[dq.front()]);     
    }
    else
    {
        result.push_back(0);
    }
        
    // 2. Process the remaining windows
    for(int i=k; i<nums.size(); i++)
    {
        // Outgoing: Remove index if it's out of window bounds
        if(!dq.empty() && dq.front() <= i-k)
        {
            dq.pop_front();
        }

        // IMPROVEMENT 1: Add the current number to dq if it's negative
        // You missed this part in your last version!
        if(nums[i] < 0) 
        {
            dq.push_back(i);
        }

        // IMPROVEMENT 2: Record the result AFTER adding the new number
        if(!dq.empty())
        {
            result.push_back(nums[dq.front()]);
        }
        else 
        {
            result.push_back(0);
        }
    }

    // 3. Print the results
    for (int val : result) 
    {
        cout << val << " ";
    }
    return 0;
}