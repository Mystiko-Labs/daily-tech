"""
Question:
Given an array of integers in an arbitrary order. Return whether it is possible to make the array
non-decreasing by modifying at most 1 element to any value.

Time Complexity: O(n)
"""

import unittest

class Solution:

	def check(self, nums):

		if len(nums) <= 1:
			return True

		v = 0

		for i in range(0, len(nums)-1):
			if nums[i] > nums[i+1]:
				v += 1

		return v <= 1

class TestCases(unittest.TestCase):

	def test_check(self):
		s = Solution()

		self.assertEqual(s.check([13, 4, 7]), True)
		self.assertEqual(s.check([5, 1, 3, 2, 5]), False)
		self.assertEqual(s.check([1, 4, 7]), True)
		self.assertEqual(s.check([13, 18, 7]), True)
		self.assertEqual(s.check([12, 7]), True)
		self.assertEqual(s.check([]), True)





