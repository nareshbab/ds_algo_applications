class Node:
	"""Node declaration for doubly linked list"""

	def __init__(self, element, next, prev):
		self._element = element
		self._next = next
		self._prev = prev


class _DoublyLinkedBase:
	"""A base class providing implementation for doubly linked list"""

	def __init__(self):
		self._header = Node(None, None, None)
		self._trailer = Node(None, None, None)
		self._header._next = self._trailer
		self._trailer.prev = self._header
		self._size = 0

	def __len__(self):
		"""Returns size of the linked list"""
		return self._size

	def is_empty(self):
		"""Returns True/False if doubly linked list is empty"""
		return self._size == 0

	def _insert_between(self, item, predecessor, successor):
		"""Adds an element to the doubly linked list"""
		newest = Node(item, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1

	def _delete_node(self, node):
		"""Removes a node from the doubly linked list"""
		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1
		element = node._element
		node._prev = node._next = node._element = None
		return element


class LinkedDeque(_DoublyLinkedBase):
	"""Doubly ended queue based on the doubly linked list"""

	def first(self):
		"""Returns first element of the queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		return self._header._next._element

	def last(self):
		"""Returns last element of the queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		return self._trailer._prev._element

	def insert_first(self, item):
		"""Insert an element at the start of the queue"""
		self._insert_between(item, self._header, self._header._next)

	def insert_last(self, item):
		"""Inserts an element at the end of the queue"""
		self._insert_between(item, self._trailer._prev, self._trailer)

	def delete_first(self):
		"""Deletes the first element of the queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		return self._delete_node(self._header._next)

	def delete_last(self):
		"""Deletes the last element of the queue"""
		if self.is_empty():
			raise Exception("Queue is empty")
		return self._delete_node(self._trailer._prev)
