"""
Question:
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) complexity

Idea:
Credit - @Pratik.Somawanshi
> Count all frequency of the 3 numbers
> Construct resultant array from the count.

Time Complexity: O(n)
Space Complexity: O(1)
"""
import unittest

class Solution:

	def sortNums(self, nums):

		counts = {1: 0, 2: 0, 3: 0}
		for i in nums:
			counts[i] += 1

		idx = 0
		for key in counts.keys():
			for i in range(idx, idx+counts[key]):
				nums[i] = key

			idx += counts[key]

		return nums

class TestCases(unittest.TestCase):

	def test_sortNums(self):
		s = Solution()
		self.assertListEqual(s.sortNums([1, 2, 3]), [1, 2, 3])
		self.assertListEqual(s.sortNums([]), [])
		self.assertListEqual(s.sortNums([1, 1, 1]), [1, 1, 1])
		self.assertListEqual(s.sortNums([3, 3, 2, 1, 3, 2, 1]), [1, 1, 2, 2, 3, 3, 3])


if __name__ == '__main__':
	s = Solution()
	print(s.sortNums([1, 2, 3, 2, 3]))