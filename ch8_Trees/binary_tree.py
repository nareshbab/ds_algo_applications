from trees import Tree


class BinaryTree(Tree):
	"""Abstract base class representing a binary tree"""

	# -----------------additional abstract method------------#
	def left(self, p):
		"""Returns a position representing left child of p"""
		raise NotImplementedError("must be implemented by base class")

	def right(self, p):
		"""Returns a position representing right child of p"""
		raise NotImplementedError("must be implemented by base class")
	
	# ------------concrete methods implemented in this class ----#
	def sibling(self, p):
		"""Returns a position representing sibling of p"""
		parent = self.parent(p)
		if parent is None:
			return None
		else:
			if p == self.left(parent):
				return self.right(p)
			else:
				return self.left(p)

	def children(self, p):
		"""Generate an iteration of Positions representing children of p"""
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)

	def inorder(self):
		"""Generates Inorder iteration of all positions of the tree
		This traversal is specifically for binary tree
		"""
		if not self.is_empty():
			for p in self._subtree_inorder(self.root()):
				yield p

	def _subtree_inorder(self, p):
		"""Generates Inorder iteration of all positions of the tree
		This traversal is specifically for binary tree
		"""
		if self.left(p):
			for other in self._subtree_inorder(self.left(p)):
				yield other
		yield p

		if self.right(p):
			for other in self._subtree_inorder(self.right(p)):
				yield other

	def positions(self):
		"""Generates an iteration of all positions"""
		return self.inorder()
