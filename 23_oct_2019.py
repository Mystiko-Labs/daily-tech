"""
Question:
Given a string, find the length of the longest substring without repeating characters

Idea:
> Iterate over the characters in the given string one by one.
> Keep a count of how many characters iterated.
> If a character is repeated, compare the previous max length with current length of substring and keep the maximum
> Reset the counter when character is repeated and start counting again.
> At the end, return the current count or previous max length

Time Complexity => O(n)

Feel free to test with more corner cases and raise an issue in case of a bug
"""

import unittest

class Solution():
    def lengthOfLongestSubstring(self, s):

        if len(s) == 1:
            return 1

        mdict = {}
        lmax = 0

        counter = 0
        for index, char in enumerate(s):
            try:
                if mdict[char]:
                    lmax = max(lmax, counter)
                    mdict = {}
                    mdict[char] = True
                    counter = 1

            except KeyError as e:
                mdict[char] = True
                counter += 1

        return max(lmax, counter)

class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_case2(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('abcddef'), 4)

    def test_case3(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('aabcdef'), 6)

    def test_case4(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('aabbcdefghhijk'), 7)

    def test_case5(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('aa'), 1)

    def test_case6(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('ab'), 2)


if __name__=="__main__":
    ans = Solution().lengthOfLongestSubstring('aabcdef')
    print(ans)