"""
Implementation of Stack using Linked list ADT
"""


class LinkedStack:
	"""Custom Stack implementation using Linked list"""


	class Node:
		"""Class to represent a single node of Linked List"""

		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		"""Create an instance of empty Stack"""
		self._head = None
		self._size = 0

	def push(self, element):
		"""Insert an element to Stack"""
		# Create new node with e as element and previous head node as next
		self._head = self.Node(element, self._head)
		self._size += 1

	def pop(self):
		"""Returns the top element of the Stack"""
		if self.is_empty():
			raise Exception("Stack is empty")
		# Get the element of head
		answer = self._head._element
		# Assign the head to next of head which points to previous node in the stack
		self._head = self._head._next
		self._size -= 1
		return answer

	def top(self):
		"""Returns the top value of the stack"""
		if self.is_empty():
			raise Exception("Stack is empty")
		return self._head._element

	def is_empty(self):
		"""Returns True/False depending whether Stack is empty or not"""
		return self._size == 0

	def __len__(self):
		"""Length of the stack"""
		return self._size