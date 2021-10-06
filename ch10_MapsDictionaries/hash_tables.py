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
from random import randrange
from unsorted_table_map import UnsortedTableMap


class HashMapBase(MapBase):
	"""Abstract base class for map using hash table with MAD compression"""

	def __init__(self, cap=11, p=109345121):
		"""Creates an empty hash table map"""
		self._table = cap * [None]
		self._n = 0
		self._prime = p
		self._scale = 1 + randrange(p - 1)
		self._shift = randrange(p)

	def hash_function(self, k):
		return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

	def __len__(self):
		"""Length of the table"""
		return self._n

	def __getitem(self, k):
		j = self.hash_function(k)
		return self._bucket_getitem(j, k)

	def __setitem__(self, k, v):
		j = self.hash_function(k)
		self._bucket_setitem(j, k, v)
		if self._n > len(self._table) // 2:
			self._resize(2 * len(self._table) - 1)

	def __delitem__(self, k):
		j = self.hash_function(k)
		self._bucket_delitem(j, k)

	def _resize(self, c):
		old = list(self.items())
		self._table = c * [None]
		self._n = 0
		for (k, v) in old:
			self[k] = v


class ChainHashMap(HashMapBase):
	"""Hash map implemented with separate chaining for collision resolution"""

	def _bucket_getitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error: ' + repr(k))
		return bucket[k]

	def _bucket_setitem(self, j, k, v):
		bucket = self._table[j]
		if bucket is None:
			self._table[j] = UnsortedTableMap()
		oldsize = len(self._table[j])
		self._table[j][k] = v
		if len(self._table[j]) > oldsize:
			self._n += 1

	def _bucket_delitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error: ' + repr(k))
		del bucket[j][k]

	def __iter__(self):
		for bucket in self._table:
			if bucket is not None:
				for key in bucket:
					yield key


class ProbeHashMap(HashMapBase):
	"""Hash map implemented with linear probing for collision resolution"""

	_AVAIL = object()       # sentinel marks location of previous deletions

	def _is_available(self, j):
		"""Returns True if the index j is present in the table"""
		return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

	def _find_slot(self, j, k):
		"""Search for key k in bucket at index j"""
		firstAvail = None
		while True:
			if self._is_available(j):
				if firstAvail is None:
					firstAvail = j
				if self._table[j] is None:
					return False, firstAvail
			elif k == self._table[j]._key:
				return True, j
			j = (j + 1) % len(self._table)

	def _bucket_setitem(self, j, k, v):
		found, s = self._find_slot(j, k)
		if not found:
			self._table[s] = self._Item(k, v)
			self._n += 1
		else:
			self._table[s]._value = v

	def _bucket_delitem(self, j, k):
		found, s = self._find_slot(j, k)
		if not found:
			raise KeyError('Key Error: ' + repr(k))
		self._table[s] = ProbeHashMap._AVAIL

	def _bucket_getitem(self, j, k):
		found, s = self._find_slot(j, k)
		if not found:
			raise KeyError('Key Error: ' + repr(k))
		return self._table[s]._value

	def __iter__(self):
		for j in range(len(self._table)):
			if not self._is_available(j):
				yield self._table[j]._key
