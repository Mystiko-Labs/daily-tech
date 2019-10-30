"""
Question:
Given a list of numbers, where every number shows up twice except for one number, find that number

Time Complexity: O(n)
Space Complexity: O(1)
"""
import unittest

class Solution:

	def findUnique(self, nums):
		res = 1
		zero = False
		for num in nums:
			if num == 0:
				zero = not zero
				continue

			if res % num == 0:
				res /= num
			else:
				res *= num

		if zero:
			return 0

		return res

class TestCases(unittest.TestCase):

	def test_findUnique(self):
		s = Solution()
		self.assertEqual(s.findUnique([1, 2, 3, 2, 3]), 1)
		self.assertEqual(s.findUnique([2, 3, 2]), 3)
		self.assertEqual(s.findUnique([2]), 2)
		self.assertEqual(s.findUnique([0, 1, 2, 2, 1]), 0)
		self.assertEqual(s.findUnique([0, 0, 1, 1, 2]), 2)


if __name__ == '__main__':
	s = Solution()