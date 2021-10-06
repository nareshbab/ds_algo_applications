class Node:

	def __init__(self, element, next):
		self._element = element
		self._next = next


class LinkedQueue:
	"""Queue implementation using Linked list"""

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def is_empty(self):
		"""Returns True/False if Queue is empty"""
		return self._size == 0

	def enqueue(self, item):
		"""Add an element to the Queue"""
		newest = Node(item, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size += 1

	def dequeue(self):
		"""Removes an element from Queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None
		return answer

	def __len__(self):
		""""""
		return self._size

	def first(self):
		"""Returns the element at the front of the Queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		return self._head._element



"""Implementing Queues with Circular Linked list"""
class CircularQueue:
	"""An implementation of Queue using circularly linked list"""

	def __init__(self):
		self._tail = None
		self._size = 0

	def __len__(self):
		"""Returns length of the Queue"""
		return self._size

	def is_empty(self):
		"""Returns True/False after checking size of the Queue"""
		return self._size == 0

	def enqueue(self, item):
		"""Add new element to the queue"""
		newest = Node(item, None)
		if self.is_empty():
			newest._next = newest
		else:
			newest._next = self._tail._next
			self._tail._next = newest
		self._tail = newest
		self._size +=1

	def dequeue(self):
		"""Removes the element from the head of the queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		oldhead = self._tail._next
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = oldhead._next
		self._size -= 1
		return oldhead._element

	def first(self):
		"""Returns the first element of the queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		answer = self._tail._next
		return answer._element

	def rotate(self):
		"""Rotates first element to the back of the Queue"""
		if self._size > 0:
			self._tail = self._tail._next   # Old head becomes the new tail
