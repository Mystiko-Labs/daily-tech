"""
Question:
Given a linked list, reverse the linked list in iterative and recursive method

"""
import unittest

class Node:
    def __init__(self, data):
        self.key = data
        self.next = None

class Solution:

    def print_llist(self, head):
        while head is not None:
            print(head.key, ' => ', end='')
            head = head.next
        print('NULL')

    def llist_to_arr(self, head):
        arr = []
        while head is not None:
            arr.append(head.key)
            head = head.next
        return arr

    def build_llist(self, arr):
        if len(arr) == 0:
            return None, None

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            node = Node(arr[i])
            tail.next = node
            tail = node

        return head, tail

    def reverseList(self, head):
        new_head = None
        while head is not None:
            node = Node(head.key)
            node.next = new_head
            new_head = node
            head = head.next

        return new_head

    def reverseListRecursive(self, head):
        if head is None:
            return None

        if head.next is None:
            return head

        rlist = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None

        return rlist

    def solve(self, arr, mode='i'):
        h, t = self.build_llist(arr)
        if mode == 'i':
            return self.reverseList(h)
        return self.reverseListRecursive(h)

class TestCases(unittest.TestCase):

    def test_reverseList(self):
        s = Solution()
        self.assertListEqual(s.llist_to_arr(s.solve([0, 1, 2, 3])), [3, 2, 1, 0])
        self.assertListEqual(s.llist_to_arr(s.solve([0])), [0])
        self.assertListEqual(s.llist_to_arr(s.solve([])), [])

    def test_reverseListRecursive(self):
        s = Solution()
        self.assertListEqual(s.llist_to_arr(s.solve([0, 1, 2, 3], mode='r')), [3, 2, 1, 0])
        self.assertListEqual(s.llist_to_arr(s.solve([0], mode='r')), [0])
        self.assertListEqual(s.llist_to_arr(s.solve([], mode='r')), [])

if __name__ == "__main__":
    s = Solution()
    h, t = s.build_llist([0, 1])
    s.reverseListRecursive(h)