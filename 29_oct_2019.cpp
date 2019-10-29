/*
Question:
Given a list of numbers and a target k, return whether or not there are two numbers in the list that add upto k.

Idea:
> Traverse the list and keep track of all the required nums for each element
> Suppose target is 10 and the list element is 3, keep track of 7 as a required number
> Whenever you find one of the required numbers return true
> If you do not any required number by the time you finish the list, return false

Time Complexity: O(n)
Space Complexity: O(n)
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool targetPresent(vector<int> nums, int target) {
        map<int, int> req;
        bool found = false;

        for (auto c: nums) {
            if (req.count(c) > 0) {
                return true;
            }
            else {
                req[target-c] = c;
            }
        }
        return false;
    }
};

int main() {
    Solution s;
    cout << s.targetPresent(vector<int>{1, -1, 3, 6}, 9) << endl;
}