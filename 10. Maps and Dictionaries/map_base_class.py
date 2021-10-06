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
from collections import MutableMapping


class MapBase(MutableMapping):
	"""Our own base class that includes a non public _Item class"""

	# ----------------nested Item class -------------------- #
	class _Item:
		"""Lightweight Composite to store key-value pairs as map items"""
		__slots__ = '_key', '_value'

		def __init__(self, key, value):
			self._key = key
			self._value = value

		def __eq__(self, other):
			""""""
			return self._key == other._key

		def __ne__(self, other):
			""""""
			return not self == other

		def __lt__(self, other):
			""""""
			return self._key < other._key
