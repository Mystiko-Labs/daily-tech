"""
Question:
Given a string s, find the longest palindromic substring in s

Idea:
Brute Force Solution:
> Iterate over all the substrings
> Check if each substring is a palindrome
> Keep track of the longest palindrome substring

Time Complexity: O(n^2)

Feel free to add more corner cases and raise an issue in case of a bug
"""
import unittest

class Solution:
    def isPalindrome(self, s):
        if s[::-1] == s:
            return True
        else:
            return False

    def longestPalindrome(self, s):
        max_str, max_len = '', 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.isPalindrome(s[i:j]):
                    if j-i > max_len:
                        max_len = j-i
                        max_str = s[i:j]

        return None if len(max_str) == 1 else max_str


class TestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_isPalindrome(self):
        self.assertTrue(self.sol.isPalindrome("ana"))
        self.assertFalse(self.sol.isPalindrome("lamp"))
        self.assertTrue(self.sol.isPalindrome("moom"))
        self.assertTrue(self.sol.isPalindrome("racecar"))

    def test_cases(self):
        f = lambda x: self.sol.longestPalindrome(x)
        self.assertEqual(f("banana"), "anana")
        self.assertTrue(f("tracecar"), "racecar")
        self.assertIsNone(f("nopalindrome"))

if __name__=="__main__":
    ans = Solution().longestPalindrome("banana")
    if ans is None:
        print("No palindromic substring found")
    else:
        print("Answer: {}".format(ans))