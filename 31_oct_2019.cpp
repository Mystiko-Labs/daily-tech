/*
Question:
Given an array of integers in an arbitrary order. Return whether it is possible to make the array
non-decreasing by modifying at most 1 element to any value.

Time Complexity: O(n)
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool check(vector<int> v) {
        int c = 0;

        for (int i=0; i<v.size()-1; i++) {
            if (v[i] > v[i+1]) {
                c++;
            }
        }

        return (bool)(c <= 1);
    }
};

int main() {
    Solution s;
    cout << s.check(vector<int>{13, 4, 7});
}
