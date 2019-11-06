"""
Question: Invert a binary tree
"""

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class Solution:

	def reverse(self, node):
		if node is None:
			return

		else:
			t = node.left
			node.left = self.reverse(node.right)
			node.right = self.reverse(t)
			return node

	def print_tree(self, root):
		stack = []
		stack.append((root, 0))
		while len(stack) != 0:
			node, indent = stack.pop(-1)
			print(f'{" " * indent}[{node.value}]')
			if node.left is not None:
				stack.append((node.left, indent + 4))
			if node.right is not None:
				stack.append((node.right, indent + 4))



if __name__ == '__main__':
	root = Node(5)
	root.left = Node(4)
	root.right = Node(6)
	root.left.left = Node(3)
	root.left.right = Node(2)
	root.right.right = Node(7)
	root.right.left = Node(8)
