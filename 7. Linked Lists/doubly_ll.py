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
