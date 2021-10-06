"""
Map class hierarchy in Python
MutableMapping
	MapBase
		UnsortedTableMap
		HashMapBase
			ChainHashMap
			ProbeHashMap
		SortedTableMap
		TreeMap
"""
from map_base_class import MapBase


class UnsortedTableMap(MapBase):
	"""Map implementation using unsorted list"""

	def __init__(self):
		"""Creates an empty map"""
		self._table = []

	def __getitem__(self, k):
		"""Returns the value of item at index k"""
		for item in self._table:
			if item._key == k:
				return item._value
		raise KeyError("Key Error: " + repr(k))

	def __setitem__(self, k, v):
		"""Sets an item in the map at position k with value v"""
		for item in self._table:
			if item._key == k:
				item._value = v
				return
		self._table.append(self._Item(k, v))

	def __delitem(self, k):
		"""Removes an item from the map"""
		for item in self._table:
			if item._key == k:
				self._table.pop(k)
				return
		raise KeyError("Key Error: " + repr(k))

	def __len__(self):
		"""Returns the length of the map"""
		return len(self._table)

	def __iter__(self):
		"""Generate an iteration of the map's keys"""
		for item in self._table:
			yield item._key
