from ch8_Trees.linked_binary_tree import LinkedBinaryTree
from ch10_MapsDictionaries.map_base_class import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
	"""Sorted map implementation using a binary search tree"""

	# ---------------- override Position class -------------- #
	class Position(LinkedBinaryTree.Position):

		def key(self):
			""""""
			pass

		def value(self):
			""""""
			pass

	# ----------------non public utilities -------------------- #
	def _subtree_search(self, p, k):
		""""""
		pass

	def _subtree_first_position(self, p):
		""""""
		pass

	def _subtree_last_position(self, p):
		""""""
		pass

	def first(self):
		""""""
		pass

	def last(self):
		""""""
		pass

	def before(self, p):
		""""""
		pass

	def after(self, p):
		""""""
		pass

	def find_position(self, k):
		""""""
		pass

	def find_min(self):
		""""""
		pass

	def find_ge(self, k):
		""""""
		pass

	def find_range(self, start, stop):
		""""""
		pass

	def __getitem__(self, k):
		""""""
		pass

	def __setitem__(self, k, v):
		""""""
		pass

	def __iter__(self):
		""""""
		pass

	def delete(self, p):
		""""""
		pass

	def __delitem__(self, k):
		""""""
		pass
