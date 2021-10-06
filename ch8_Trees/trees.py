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


class Tree:
	"""Abstract base class representing a tree structure"""
	# --------------------nested Position class----------#
	class Position:
		"""Abstraction representing the location of a single element"""

		def element(self):
			"""Returns the element stored at this position"""
			raise NotImplementedError("must be implemented by subclass")

		def __eq__(self, other):
			"""Returns True if other Position represents the same location"""
			raise NotImplementedError("must be implemented by subclass")

		def __ne__(self, other):
			"""Returns True if other Position is not equal to the same location"""
			raise NotImplementedError("must be implemented by subclass")

	# -------------------abstract methods base class must support---------#
	def root(self):
		"""Returns the position of root element (None if empty)"""
		raise NotImplementedError("must be implemented by subclass")

	def parent(self, p):
		"""Returns the position of the parent of p (None if root)"""
		raise NotImplementedError("must be implemented by subclass")

	def num_children(self, p):
		"""Returns the number of children of position p"""
		raise NotImplementedError("must be implemented by subclass")

	def children(self, p):
		"""Returns the iterator for positions of p's children"""
		raise NotImplementedError("must be implemented by subclass")

	def __len__(self):
		"""Returns the total number of elements in the tree"""
		raise NotImplementedError("must be implemented by subclass")

	# ---------concrete methods implemented in this class----#
	def is_root(self, p):
		"""Returns True if Position p is the root of the tree"""
		return self.root() == p

	def is_leaf(self, p):
		"""Returns True if Position p is a leaf node"""
		return self.num_children(p) == 0

	def is_empty(self):
		"""Returns True if the tree is empty
		Time complexity: O(1)
		"""
		return len(self) == 0

	def depth(self, p):
		"""Returns the number of level separating p from the root
		Time complexity: O(Dp +1)
		Dp -> depth of node at position p, worst case is O(n)
		"""
		return 1 + self.depth(self.parent(p))

	def _height1(self):
		"""Returns the height of the tree
		Time complexity: O(n2)
		n for iterating all the nodes to check if its a leaf
		other n for calculating the depth of every leaf node
		"""
		return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

	def _height2(self, p):
		"""Returns the height of the tree rooted at position p
		Time complexity: O(n)
		"""
		return 1 + max(self._height2(c) for c in self.children(p))

	def height(self, p=None):
		"""Returns the height of the tree rooted at p
		If p is None, returns the height of the entire tree
		Time complexity: O(n)
		"""
		if p is None:
			p = self.root()
		return self._height2(p)

	# -----------traversal methods ------------- #
	def __iter__(self):
		"""Generate an iteration of tree's elements"""
		for p in self.positions():
			yield p.element()

	def preorder(self):
		"""Generate a preorder iteration of the tree's positions"""
		if not self.is_empty():
			for p in self._subtree_preorder(self.root()):
				yield p

	def _subtree_preorder(self, p):
		"""Preorder traversal of trees nodes"""
		yield p
		for c in self.children(p):
			for other in self._subtree_preorder(c):
				yield other

	def positions(self):
		"""Generate an iteration of tree's positions"""
		# This can be replaced with postorder , inorder or any other traversal algorithm
		return self.inorder()

	def postorder(self):
		"""Generates Postorder iteration of all positions of the tree"""
		if not self.is_empty():
			for p in self._subtree_preorder(self.root()):
				yield p

	def _subtree_postorder(self, p):
		"""Generates Postorder iteration of all positions of the tree"""
		for c in self.children(p):
			for other in self._subtree_preorder(c):
				yield other
		yield p

	def breadthfirst(self):
		"""Generates bread first iteration of all positions of the tree"""
		if not self.is_empty():
			fringe = LinkedQueue()
			fringe.enqueue(self.root())
			while not fringe.is_empty():
				p = fringe.dequeue()
				yield p
				for c in self.children(p):
					fringe.enqueue(c)
