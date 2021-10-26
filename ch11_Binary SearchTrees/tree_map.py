from ch8_Trees.linked_binary_tree import LinkedBinaryTree
from ch10_MapsDictionaries.map_base_class import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
	"""Sorted map implementation using a binary search tree"""

	# ---------------- override Position class -------------- #
	class Position(LinkedBinaryTree.Position):

		def key(self):
			"""Return key of map's key-value pair"""
			return self.element()._key

		def value(self):
			"""Return value of map's key-value pair"""
			return self.element()._value

	# ----------------non public utilities -------------------- #
	def _subtree_search(self, p, k):
		"""Return Position of p's subtree having key k, or last node searched"""
		if k == p.key():
			return p
		elif k < p.key():
			return self._subtree_search(self.left(p), k)
		else:
			if self.right(p) is not None:
				return self._subtree_search(self.right(p), k)
		return p

	def _subtree_first_position(self, p):
		"""Return Position of first item in the subtree rooted at p"""
		walk = p
		while self.left(walk) is not None:
			walk = self.left(walk)
		return walk

	def _subtree_last_position(self, p):
		"""Return Position of last item in the subtree rooted at p"""
		walk = p
		while self.right(walk) is not None:
			walk = self.right(walk)
		return walk

	def first(self):
		"""Return the first Position of the tree or None if empty"""
		return self._subtree_first_position(self.root()) if len(self) > 0 else None

	def last(self):
		"""Return the last Position of the tree or None if empty"""
		return self._subtree_last_position(self.root()) if len(self) > 0 else None

	def before(self, p):
		"""
		Return the Position just before p in natural order
		Return None if p is the first position
		"""
		self._validate(p)
		if self.left(p):
			return self._subtree_last_position(self.left(p))
		else:
			# walk upward
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.left(above):
				walk = above
				above = self.parent(walk)
			return above

	def after(self, p):
		"""Return the Position just after p in natural order
		Return None if p is the first position"""
		self._validate(p)
		if self.right(p):
			return self._subtree_first_position(self.right(p))
		else:
			# walk upward
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.right(p):
				walk = above
				above = self.parent(walk)
			return above

	def find_position(self, k):
		"""Return position with key k or else neighbor"""
		if self.is_empty():
			return None
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			return p

	def find_min(self):
		"""Return tkey, value pair with minimum key"""
		if self.is_empty():
			return None
		else:
			p = self.first()
			return p.key(), p.value()

	def find_ge(self, k):
		"""Return key, value pair with least key greater than or equal to k"""
		if self.is_empty():
			return None
		else:
			p = self.find_position(k)
			if p.key() < k:
				p = self.after(p)
			return p.key(), p.value() if p is not None else None

	def find_range(self, start, stop):
		"""
		Iterate all key, value pairs such that start <= key < stop
		If start is None then start = first
		If stop is None then stop = last
		"""
		if not self.is_empty():
			if start is None:
				p = self.first()
			else:
				p = self.find_position(start)
				if p.key() < start:
					p = self.after(p)
			while p is not None and (stop is None or p.key() < stop):
				yield p.key(), p.value()
				p = self.after(p)

	def __getitem__(self, k):
		"""Return value associated with key k or raise KeyError"""
		if self.is_empty():
			raise KeyError('Key Error: ' + repr(k))
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			if k != p.key():
				raise KeyError('Key Error: ' + repr(k))
			return p.value()

	def __setitem__(self, k, v):
		"""Assign value v to key k, overwrite the exisiting if any"""
		if self.is_empty():
			leaf = self._add_root(self._Item(k, v))
		else:
			p = self._subtree_search(self.root(), k)
			if p.key() == k:
				p.element()._value = v
				self._rebalance_access(p)
				return
			else:
				item = self._Item(k, v)
				if p.key() < k:
					leaf = self._add_right(p, item)
				else:
					leaf = self._add_left(p, item)
		self._rebalance_access(leaf)

	def __iter__(self):
		"""Generate key, value for all the keys in the map"""
		p = self.first()
		while p is not None:
			yield p.key()
			p = self.after(p)

	def delete(self, p):
		"""Remove the item at Position p"""
		self._validate(p)
		if self.left(p) and self.right(p):
			replacement = self._subtree_last_position(self.left(p))
			self._replace(p, replacement.element())
		parent = self.parent(p)
		self._delete(p)
		self._rebalance_access(parent)

	def __delitem__(self, k):
		"""Remove the item associated with key k"""
		if not self.is_empty():
			p = self._subtree_search(self.root(), k)
			if k == p.key():
				self.delete(p)
				return
			self._rebalance_access(p)
		raise KeyError('Key Error: ' + repr(k))
