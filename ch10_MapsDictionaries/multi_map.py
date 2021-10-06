class MultiMap:
	"""A multimap class built upon use of an underlying map for storage"""
	_MapType = dict

	def __init__(self):
		"""Create a new empty multimap instance"""
		self._map = self._MapType()
		self._n = 0

	def __iter__(self):
		"""Iterate through all key, value pairs in multimap"""
		for k, secondary in self._map.items():
			for v in secondary:
				yield k, v

	def add(self, k, v):
		"""Add pair k, v to multimap"""
		# Return the container if key k is present or set and return an empty list
		container = self._map.setdefault(k, [])
		container.append(v)
		self._n += 1

	def pop(self, k):
		"""Remove and return arbitrary k, v with key k or raise KeyError"""
		secondary = self._map[k]
		# Pop a random value from map
		v = secondary.pop()
		if len(secondary) == 0:
			del self._map[k]
		self._n -= 1
		return k, v

	def find(self, k):
		"""Return the key k or raise key error"""
		secondary = self._map.get(k)
		if secondary:
			return k, secondary
		else:
			raise KeyError("Key Error: " + repr(k))

	def find_all(self, k):
		"""Generate an iteration of pair k, v for all values of key k"""
		secondary = self._map.get(k, [])
		for v in secondary:
			yield k, v
