from .binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
	"""Linked representation of binary tree structure"""

	class Node: # Lightweight, non public class for storing node

		__slots__ = '_element', '_parent', '_left', '_right'

		def __init__(self,  element, parent=None, left=None, right=None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right


	class Position(BinaryTree.Position):
		"""An abstraction representing the location of a single element"""

		def __init__(self, container, node):
			"""Constructor for Position"""
			self._container = container
			self._node = node

		def element(self):
			"""Returns the element of the Position"""
			return self._node._element

		def __eq__(self, other):
			"""Returns True if other is equal to the same Position"""
			return type(other) is type(self) and other._node is self._node

	def _validate(self, p):
		"""Returns associated node if position is valid"""
		if not isinstance(p, self.Position):
			raise TypeError("p must be instance of Position")
		if p._container is not self:
			raise ValueError("p does not belong to this container")
		if p._node._parent is p._node: # convention for deprecated nodes
			raise ValueError("p is no longer valid")
		return p._node

	def _make_position(self, node):
		"""Returns the Position instance for a node"""
		return self.Position(self, node) if node is not None else None

	# -----constructor for linked binary tree------#
	def __init__(self):
		"""Creates and initial empty binary tree"""
		self._root = None
		self._size = 0

	# -----------public accessors-------------#
	def __len__(self):
		"""Returns the total number of elements in a tree"""
		return self._size

	def root(self):
		"""Returns the position representing root node of the tree"""
		return self._make_position(self._root)

	def parent(self, p):
		"""Returns the position representing parent of the p's position"""
		node = self._validate(p)
		return self._make_position(node._parent)

	def left(self, p):
		"""Returns the position representing left child of p's position"""
		node = self._validate(p)
		return self._make_position(node._left)

	def right(self, p):
		"""Returns the position representing right child of p's position"""
		node = self._validate(p)
		return self._make_position(node._right)

	def num_children(self, p):
		"""Returns the number of children of position p"""
		node = self._validate(p)
		count = 0
		if node._left:
			count += 1
		if node._right:
			count += 1
		return count

	def _add_root(self, e):
		"""Place element e at the root of empty tree and return the position
		Raise ValueError if tree non empty
		"""
		if self._root:
			raise ValueError("Tree is not empty")
		self._size += 1
		self._root = self.Node(element=e)
		return self._make_position(self._root)

	def _add_left(self, p, e):
		"""Create a new left child of position p storing element e
		Return position of the new node
		Raise ValueError if left node is not empty
		"""
		node = self._validate(p)
		if node._left:
			raise ValueError("left child already exists")
		self._size += 1
		node._left = self.Node(element=e, parent=node)
		return self._make_position(node._left)


	def _add_right(self, p, e):
		"""Create a new right child of position p storing element e
		Return position of the new node
		Raise ValueError if right node is not empty"""
		node = self._validate(p)
		if node._right:
			raise ValueError("right child already exists")
		self._size += 1
		node._right = self.Node(element=e, parent=node)
		return self._make_position(node._right)

	def _replace(self, p, e):
		"""Replace the position p's element with e"""
		node = self._validate(p)
		old = node._element
		node._element = e
		return old

	def _delete(self, p):
		"""Deletes the node at position p and replaces it with its child node
		Return the element that had been stored at Position p
		Raise ValueError if Position p is invalid or p has 2 children
		"""
		node = self._validate(p)
		if self.num_children(p) == 2:
			raise ValueError("Node has 2 children")
		child = node._left if node._left else node._right

		# Change the parent of the child if child is not None
		if child:
			child._parent = node._parent

		# If node is root then make child as new root
		if node is self._root:
			self._root = child
		else:
			# Depending upon whether node is left child or right child
			# Assign the child to parents specific location i.e left or right
			parent = node._parent
			if node is parent._left:
				parent._left = child
			else:
				parent._right = child
		self._size -= 1
		# Deprecate the node
		node._parent = None
		return node._element

	def _attach(self, p, t1, t2):
		"""Attach trees t1 and t2 as left and right subtrees of external p"""
		node = self._validate(p)
		if not self.is_leaf(p):
			raise ValueError("position must be a leaf node")

		if not type(self) is type(t1) is type(t2):
			raise TypeError("Trees must be of similar type")

		self._size = len(t1) + len(t2)

		if not t1.is_empty():
			t1._root._parent = node
			node._left = t1._root
			t1._root = None
			t1._size = 0

		if not t2.is_empty():
			t2._root._parent = node
			node._right = t2._root
			t2._root = None
			t2._size = 0
