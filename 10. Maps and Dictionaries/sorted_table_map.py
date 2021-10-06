from map_base_class import MapBase


class SortedTableMap(MapBase):
	"""Map implementation using sorted table"""

	# ------------non public behavior ----------------#
	def _find_index(self, k, start, end):
		"""
		Return the key with left most item with key >= k
		Returns end + 1 if no such item qualifies
		That is j will be returned such that
			all items of slice table[start:j] have key < k
			all items of slice table[j:end+1] have key >= k
		"""
		if start > end:
			return end + 1
		else:
			mid = start + (end - start) // 2
			if k == self._table[mid]._key:
				return mid
			elif k > self._table[mid]._key:
				return self._find_index(k, mid + 1, end)
			else:
				return self._find_index(k, start, mid - 1)

	# --------------public behaviours --------------#

	def __init__(self):
		"""Creates and empty map"""
		self._table = []

	def __len__(self):
		"""Returns the length of the map"""
		return len(self._table)

	def __getitem__(self, k):
		"""
		Returns the value associated with key k
		Returns KeyError if key is not found
		"""
		j = self._find_index(k, 0, len(self._table) - 1)
		# j == len(self._table) -> element not found in the table
		# self._table[j]._key != k -> the key is not equal to the key being searched
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('Key Error: ' + repr(k))
		return self._table[j]._key

	def __setitem__(self, k, v):
		"""Assign value v to key k, overwriting existing value if it exists"""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			self._table[j]._value = v
		else:
			self._table.insert(j, self._Item(k, v))

	def __delitem__(self, k):
		"""Deletes the key k from the map"""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('Key Error: ' + repr(k))
		del self._table[j]

	def __iter__(self):
		"""Generates an iterator of all the keys in the map"""
		for item in self._table:
			yield item._key

	def __reversed__(self):
		"""Generate keys of the map ordered from maximum to minimum"""
		for item in reversed(self._table):
			yield item._key

	def find_min(self):
		"""Return (key, value) pair with minimum key"""
		if len(self._table) > 0:
			return self._table[0]._key, self._table[0]._value

	def find_max(self):
		"""Return key,value pair with maximum key"""
		if len(self._table) > 0:
			return self._table[-1]._key, self._table[-1]._value

	def find_ge(self, k):
		"""Return key, value pair with least key >= k"""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table):
			return self._table[j]._key, self._table[j]._value
		else:
			return None

	def find_lt(self, k):
		"""Return key, value pair with greatest key < k"""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j > 0:
			return self._table[j - 1]._key, self._table[j - 1]._value
		else:
			return None

	def find_gt(self, k):
		"""Returns key, value pair with least key > k"""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			j += 1
		if j < len(self._table):
			return self._table[j]._key, self._table[j]._value
		else:
			return None

	def find_range(self, start, stop):
		"""Iterate all key, value pairs such that start <= key <= stop"""
		if start is None:
			j = 0
		else:
			j = self._find_index(start, 0, len(self._table) - 1)
		while j < len(self._table) and (stop is None or self._table[j]._key < stop):
			yield self._table[j]._key, self._table[j]._value
			j += 1
