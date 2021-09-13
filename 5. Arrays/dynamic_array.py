import ctypes

class DynamicArray:
	"""Custom implementation of dynamic array"""

	def __init__(self):
		self._n = 0                                     # Current index
		self._capacity = 1                              # Capacity of array
		self._A = self._make_array(self._capacity)      # Create new array

	def __len__(self):
		"""Returns the size of the array"""
		return self._n

	def __getitem__(self, item):
		"""returns a specific index item"""
		if not 0 <= item < self._n:
			raise IndexError("Index out of range")
		return self._A[item]

	def _resize(self, c):
		"""Resizes the array to new length c"""
		B = self._make_array(c)
		for item in self._A:
			B[item] = self._A[item]
		self._A = B
		self._capacity = c

	def append(self, obj):
		"""Appends an object to the array"""
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		self._A[self._n] = obj
		self._n += 1

	def _make_array(self, c):
		"""Returns a new array of length c"""
		return (c * ctypes.py_object)()
