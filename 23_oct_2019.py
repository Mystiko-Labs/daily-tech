"""
Question:
Given a string, find the length of the longest substring without repeating characters

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
        sstart = 0
        for index, char in enumerate(s):

            try:
                previdx = mdict[char]
                mdict[char] = index
                counter = index - max(previdx, sstart-1)
                print(' ', max(previdx, sstart), end='')
                sstart = max(sstart, previdx + 1)

            except KeyError as e:
                mdict[char] = index
                counter += 1

            lmax = max(lmax, counter)
            print('|', char, index, counter, lmax, mdict, sstart)

        return max(lmax, counter)


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_cases(self):
        self.assertEqual(self.sol.lengthOfLongestSubstring('abcdefghijklmnopqrstuvwxyz'), 26)
        self.assertEqual(self.sol.lengthOfLongestSubstring('abcddef'), 4)
        self.assertEqual(self.sol.lengthOfLongestSubstring('aabcdef'), 6)
        self.assertEqual(self.sol.lengthOfLongestSubstring('aabbcdefghhijk'), 7)
        self.assertEqual(self.sol.lengthOfLongestSubstring('aa'), 1)
        self.assertEqual(self.sol.lengthOfLongestSubstring('ab'), 2)
        self.assertEqual(self.sol.lengthOfLongestSubstring('dvdf'), 3)
        self.assertEqual(self.sol.lengthOfLongestSubstring('tmmzuxt'), 5)
        self.assertEqual(self.sol.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(self.sol.lengthOfLongestSubstring('wobgrovw'), 6)
        self.assertEqual(self.sol.lengthOfLongestSubstring('zwnigfunjwz'), 8)


if __name__=="__main__":
    ans = Solution().lengthOfLongestSubstring("zwnigfunjwz")
    print(ans)