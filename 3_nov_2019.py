"""
Question:
Implement a class for a stack that supports all the regular functions (push, pop) and an additional function
of max() which returns the maximum element in the stack (return None if stack is empty). Each method should run in constant time.
"""

class Stack:
	def __init__(self):

		self.stack = []
		self.max_stack = []
		self.max = None

	def push(self, num):

		self.stack.append(num)
		if self.max is None:
			self.max = num
			self.max_stack.append((num, 1))
			return

		if num == self.max:
			t = self.max_stack[-1]
			self.max_stack[-1] = (t[0], t[1]+1)
			return

		if num > self.max:
			self.max = num
			self.max_stack.append((num, 1))


	def pop(self):

		num = self.stack.pop(-1)
		if num < self.max:
			return

		if num == self.max:
			t = self.max_stack[-1]
			if t[1] <= 1:
				self.max_stack.pop(-1)
				self.max = self.max_stack[-1][0]
			else:
				self.max_stack[-1] = (t[0], t[1]-1)


	def reset(self):
		self.stack = []
		self.max_stack = []

	def print(self):
		print('Stack')
		for i in range(len(self.stack)-1, -1, -1):
			print(self.stack[i])

		print('Max Stack')
		for i in range(len(self.max_stack)-1, -1, -1):
			print(self.max_stack[i])