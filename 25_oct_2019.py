"""
Question:
Given a string containing just the characters '{', '(', ')', '}', '[', and ']', determine if the string is valid
An input string is valid if -
> Open brackets are closed by the same type of bracket
> Open brackets are closed in the same order
> Note than an empty string is also considered valid
"""
import unittest

class Solution:

    def isValid(self, string):
        if len(string) == 0:
            return True

        pmap = {'{': '}', '(': ')', '[': ']'}
        stack, top = [], -1

        for char in string:
            if top < 0:
                stack.append(char)
                top += 1
                continue

            stop = stack[top]
            try:
                if char == pmap[stop]:
                    stack.pop(top)
                    top -= 1
                    continue
            except KeyError as e:
                return False

            stack.append(char)
            top += 1

        return top < 0

class TestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_isValid(self):
        self.assertTrue(self.sol.isValid('()()()'))
        self.assertTrue(self.sol.isValid('({})[]'))
        self.assertTrue(self.sol.isValid('[[((){})]]'))
        self.assertTrue(self.sol.isValid(''))

        self.assertFalse(self.sol.isValid('()(()'))
        self.assertFalse(self.sol.isValid('{[}{]]{}'))
        self.assertFalse(self.sol.isValid('{]'))

if __name__ == "__main__":
    print(Solution().isValid('{[}{]]{}'))