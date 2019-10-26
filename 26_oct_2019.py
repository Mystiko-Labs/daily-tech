"""
Question:
Given a sorted array A, with possibly duplicated elements, find the indices of the first and last occurrences of the
target element x. Return -1 if target not found

Idea:
> Do a binary search for the target element
> Check left side of found element for first occurrence
> Check right side of found element for last occurrence

Time Complexity: Average Case => Omega(logn)
                 Worst Case   => O(n)
"""
import unittest

class Solution:

    def binarySearch(self, arr, x):
        a, b = 0, len(arr)-1
        if len(arr) < 1:
            return -1

        while True:
            if arr[a] == x:
                return a

            if arr[b] == x:
                return b

            mid = (a + b) // 2
            if arr[mid] == x:
                return mid

            if x < arr[mid]:
                b = mid-1

            if x > arr[mid]:
                a = mid+1

            if a >= b:
                return -1


    def getRange(self, arr, x):
        target = self.binarySearch(arr, x)
        lidx = target
        fidx = target

        if target != -1:
            # Count forward
            while True:
                if lidx == len(arr) - 1:
                    break

                if arr[lidx] != arr[lidx+1]:
                    break

                lidx += 1

            # Count backward
            while True:
                if fidx == 0:
                    break

                if arr[fidx] != arr[fidx-1]:
                    break

                fidx -= 1

        return fidx, lidx

class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_binarySearch(self):
        self.assertEqual(self.sol.binarySearch([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(self.sol.binarySearch([101, 203, 406, 991], 991), 3)
        self.assertEqual(self.sol.binarySearch([1], 1), 0)
        self.assertEqual(self.sol.binarySearch([1], 2), -1)
        self.assertEqual(self.sol.binarySearch([1, 2, 3, 4, 5], 7), -1)
        self.assertEqual(self.sol.binarySearch([10, 20, 30, 40], 10), 0)

    def test_getRange(self):
        self.assertTupleEqual(self.sol.getRange([1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9), (6, 8))
        self.assertTupleEqual(self.sol.getRange([100, 150, 150, 153], 150), (1, 2))
        self.assertTupleEqual(self.sol.getRange([1, 2, 3, 4, 5, 6, 10], 9), (-1, -1))
        self.assertTupleEqual(self.sol.getRange([10, 20, 30, 40], 10), (0, 0))
        self.assertTupleEqual(self.sol.getRange([1, 1000], 1000), (1, 1))
        self.assertTupleEqual(self.sol.getRange([20], 1), (-1, -1))

if __name__=="__main__":
    s = Solution()
    print(s.getRange([10, 20, 30, 40], 10))
