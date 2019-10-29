/*
Question:
Given a string containing just the characters '{', '(', ')', '}', '[', and ']', determine if the string is valid
An input string is valid if -
> Open brackets are closed by the same type of bracket
> Open brackets are closed in the same order
> Note than an empty string is also considered valid
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        map<char, char> vmap = {{'{', '}'}, {'[', ']'}, {'(', ')'}};
        char cchar;

        for (auto c: s) {
            if (stack.empty()) {
                stack.push_back(c);
                continue;
            }
            cchar = stack[stack.size()-1];
            try {
                if (c == vmap[cchar]) {
                    stack.pop_back();
                    continue;
                }
            }
            catch (...) {
                return false;
            }
            stack.push_back(c);
        }

        return (bool) stack.empty();
    }
};

int main() {
    Solution s;
    cout << s.isValid("()()()");
}