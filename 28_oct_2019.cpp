/*
Question:
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) complexity

Idea:
Credit - @Pratik.Somwanshi
> Count all frequency of the 3 numbers
> Construct resultant array from the count.

Time Complexity: O(n)
Space Complexity: O(1)
*/

#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> sortUnique(vector<int> nums) {
        map<int, int> imap = {{1, 0}, {2, 0}, {3, 0}};

        for (auto i: nums) {
            imap[i]++;
        }

        int idx = 0;
        for (auto c: imap) {
            for (int i=idx; i<idx + c.second;i++) {
                nums[i] = c.first;
            }
            idx += c.second;
        }

        return nums;
    }
};

int main() {
    Solution s;
    for (auto c: s.sortUnique(vector<int>{1, 2, 3, 3, 2, 2, 1})) {
        cout << c << ' ';
    }
    cout << endl;
}
