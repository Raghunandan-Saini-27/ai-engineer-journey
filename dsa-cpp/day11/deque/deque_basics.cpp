#include <iostream>
#include <deque>

using namespace std;

int main() {
    deque<int> dq = {1, 2, 3, 4, 5};

    dq.push_front(0);
    dq.push_back(6);
    dq.pop_front();
    dq.pop_back();
    
    cout << "First element: " << dq.front() << endl;
    cout << "Last element: " << dq.back() << endl;

    return 0;
}