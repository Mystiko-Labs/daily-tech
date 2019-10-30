"""
Question:
Given a list of numbers, where every number shows up twice except for one number, find that number

Idea:
Credits - @Pratik.Somwanshi
> Take XOR of all the numbers. Same numbers will cancel out each other.

Time Complexity: O(n)
Space Complexity: O(1)
"""
import unittest
from functools import reduce

class Solution:

	def findUnique(self, nums):
		return reduce(lambda x, y: x ^ y, nums)

class TestCases(unittest.TestCase):

	def test_findUnique(self):
		s = Solution()
		self.assertEqual(s.findUnique([1, 2, 3, 2, 3]), 1)
		self.assertEqual(s.findUnique([2, 3, 2]), 3)
		self.assertEqual(s.findUnique([2]), 2)
		self.assertEqual(s.findUnique([0, 1, 2, 2, 1]), 0)
		self.assertEqual(s.findUnique([0, 0, 1, 1, 2]), 2)
		self.assertEqual(s.findUnique([0, 0, 1, 1, 2]), 2)


if __name__ == '__main__':
	s = Solution()