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
    
    def isPalindrome(self, s, i, j):
        if i == j:
            return True

        if i == j-1:
            return s[i] == s[j]

        # print(i, j)
        # print(s[i], s[j])
        return self.isPalindrome(s, i+1, j-1) and s[i] == s[j]

    def longestPalindrome(self, s):
        if s == '':
            return ''

        max_str, max_len = '', 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    # print(s[i:j+1], i, j, max_len)
               
                   if j-i+1 > max_len:
                        max_len = j-i + 1
                        max_str = s[i:j+1]

        return s[0] if max_len <= 1 else max_str


class TestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_isPalindrome(self):
        self.assertTrue(self.sol.isPalindrome("ana", 0, 2))
        self.assertFalse(self.sol.isPalindrome("lamp", 0, 3))
        self.assertTrue(self.sol.isPalindrome("moom", 0, 3))
        self.assertTrue(self.sol.isPalindrome("racecar", 0, 6))

    def test_cases(self):
        f = lambda x: self.sol.longestPalindrome(x)
        self.assertEqual(f("banana"), "anana")
        self.assertTrue(f("tracecar"), "racecar")
        self.assertEqual(f("nopalindrome"), "n")

if __name__=="__main__":
    ans = Solution().longestPalindrome("cbbd")
    print(ans)
    # if ans is None:
    #     print("No palindromic substring found")
    # else:
    #     print("Answer: {}".format(ans))