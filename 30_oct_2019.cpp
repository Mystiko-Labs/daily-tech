/*
Question:
Given a list of numbers, where every number shows up twice except for one number, find that number

Idea:
Credits - @Pratik.Somwanshi
> Take XOR of all the numbers. Same numbers will cancel out each other.

Time Complexity: O(n)
Space Complexity: O(1)
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findUnique(vector<int> nums) {
        int p = 0;
        for (auto c: nums) {
        	p = p ^ c;
        }
        return p;
    }
};

int main() {
    Solution s;
    int a = s.findUnique(vector<int>{0, 2, 1, 1, 2, 3, 4, 4, 3});
    cout << a << endl;
}