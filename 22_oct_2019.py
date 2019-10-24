"""
Question:
Given two linked lists containing non-negative integers in reverse order, get their addition in the form of a linked
list in reverse order

Idea:
> Add the initial node values, if carry generated, keep track of it
> Add the next node values and add the carry from the previous addition (update carry for this addition)
> If one of the nodes is None, consider it as 0 value
> Return the formed linkedlist

Time Complexity => O(n)

Feel free to test with more corner cases and raise an issue in case of a bug
"""
import unittest

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:

	def addTwoNumbers(self, l1, l2):
		
		carry = 0

		list_head = None
		list_curr = None

		while True:

			if l1 == None and l2 == None:
				break

			if l1 == None and l2 != None:
				l1_val = 0
				l2_val = l2.val
				l2 = l2.next

			if l1 != None and l2 == None:
				l1_val = l1.val
				l2_val = 0
				l1 = l1.next

			if l1 != None and l2 != None:
				l1_val = l1.val
				l2_val = l2.val
				l1 = l1.next
				l2 = l2.next

			current = l1_val + l2_val + carry

			carry = 0
			if current > 9:
				current = (current % 10)
				carry = 1

			if list_head == None:
				list_head = ListNode(current)
				list_curr = list_head

			else:
				list_curr.next = ListNode(current)
				list_curr = list_curr.next




		return list_head

	def printList(self, li):
		while li != None:
			print("{} => ".format(li.val), end='')
			li = li.next
		print()

class TestCases(unittest.TestCase):

	def num_to_llist(self, num):
		num = str(num)[::-1]
		list_head = None
		list_curr = None
		for i in num:
			if list_head is None:
				list_head = ListNode(int(i))
				list_curr = list_head
			else:
				list_curr.next = ListNode(int(i))
				list_curr = list_curr.next

		return list_head

	def llist_to_num(self, llist):
		num = ''
		while llist != None:
			num += str(llist.val)
			llist = llist.next

		num = num[::-1]
		return int(num)

	def test_conversion(self):
		f = lambda x: self.llist_to_num(self.num_to_llist(x))
		self.assertEqual(f(123), 123)
		self.assertEqual(f(100), 100)
		self.assertEqual(f(205), 205)

	def test_cases(self):
		s = Solution()
		f = lambda x, y: self.llist_to_num(s.addTwoNumbers(self.num_to_llist(x), self.num_to_llist(y)))

		self.assertEqual(f(100, 200), 300)
		self.assertEqual(f(200, 99), 299)
		self.assertEqual(f(345, 465), 810)
		self.assertEqual(f(342, 465), 807)
		self.assertEqual(f(1, 235), 236)
		self.assertEqual(f(10, 2011), 2021)


if __name__=="__main__":

	l1 = ListNode(5)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)

	s = Solution()

	print('List 1')
	s.printList(l1)
	print('List 2')
	s.printList(l2)

	sol = s.addTwoNumbers(l1, l2)
	print('Result')
	s.printList(sol)

