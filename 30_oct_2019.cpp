/*
Question:
Given a list of numbers, where every number shows up twice except for one number, find that number

Time Complexity: O(n)
Space Complexity: O(1)
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findUnique(vector<int> nums) {
        int p = 1;
        bool zero = false;

        for(auto c: nums) {
            if (c == 0) {
                zero = !zero;
                continue;
            }
            if (p % c ==0) {
                p /= c;
            }
            else {
                p *= c;
            }
        }

        if (zero) {
            return 0;
        }

        return p;
    }
};

int main() {
    Solution s;
    int a = s.findUnique(vector<int>{0, 2, 1, 1, 2, 3, 4, 4, 3});
    cout << a << endl;
}