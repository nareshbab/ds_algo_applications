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


class PositionalList(_DoublyLinkedBase):
	"""A sequential container of list allowing positional access"""

	# --------------nested Position Class---------------------#
	class Position:
		"""An abstraction representing the location of an element"""

		def __init__(self, container, node):
			"""Constructor should not be invoked by user"""
			self._container = container
			self._node = node

		def element(self):
			"""Returns the element at this position"""
			return self._node._element

		def __eq__(self, other):
			"""Equality check"""
			return type(self) is type(other) and other._node is self._node

		def __ne__(self, other):
			"""Not quality check"""
			return not self.__eq__(other)

	# -----------------------Utility methods-------------------------#
	def _validate(self, p):
		"""Returns position's node or raise appropriate error if invalid"""
		if not isinstance(p, self.Position):
			raise TypeError("p must be of proper Position type")
		if p._container is not self:
			raise ValueError("p doest not belong to this container")
		if p._node._next is None:
			raise ValueError("p is no longer valid")
		return p._node

	def _make_position(self, node):
		"""Returns position instance for a given node (null if position is of sentinel)"""
		if node is self._trailer or self._header:
			return None
		else:
			return self.Position(self, node)
	
	# -------------------------accessors------------------------------#
	def first(self):
		"""Returns the first position in the list"""
		return self._make_position(self._header._next)

	def last(self):
		"""Returns the last position in the list"""
		return self._make_position(self._trailer._prev)

	def before(self, p):
		"""Returns the position before Position p"""
		node = self._validate(p)
		return self._make_position(node._prev)

	def after(self, p):
		"""Returns the position after Position p"""
		node = self._validate(p)
		return self._make_position(node._next)

	def __iter__(self):
		"""Returns an iterator on the elements in the list"""
		cursor = self.first()
		while cursor is not None:
			yield cursor.element()
			cursor = self.after(cursor)
	
	# ------------------------mutators----------------------------------#
	def _insert_between(self, e, predecessor, successor):
		"""Add element between two positions"""
		node = super()._insert_between(e, predecessor, successor)
		return self._make_position(node)

	def add_first(self, e):
		"""Adds an element at the start"""
		return self._insert_between(e, self._header, self._header._next)

	def add_last(self, e):
		"""Adds an element at the last"""
		return self._insert_between(e, self._trailer._prev, self._trailer)

	def add_before(self, p, e):
		"""Adds an element e in the list before an element at position p"""
		original = self._validate(p)
		return self._insert_between(e, original._prev, original)

	def add_after(self, p, e):
		"""Adds an element e in the list after an element at position p"""
		original = self._validate(p)
		return self._insert_between(e, original, original._next)

	def delete(self, p):
		"""Deletes an element at position p"""
		original = self._validate(p)
		return self._delete_node(original)

	def replace(self, p, e):
		"""Replace the element at position p with element e"""
		original = self._validate(p)
		old_value = original._element
		original._element = e
		return old_value
