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

	def insert(self, k, value):
		"""Inserts a value at specific index"""
		# IMP:: If we have to insert element then navigate from reverse order
		if self._n == self._capacity:
			self._resize(1 * self._capacity)
		for i in range(self._n, k, -1):         # First make space for new element
			self._A[i] = self._A[i-1]           # Shift all elements from k to n-1 by 1
		self._A[k] = value
		self._n += 1

	def remove(self, value):
		"""Removes the first occurrence of the element
		We do not shrink the array in this method
		"""
		# IMP:: If we have to drop/remove an element then navigate in normal order
		for i in range(self._n):
			if self._A[i] == value:
				for j in range(i, self._n - 1):
					self._A[j] = self._A[j+1]
				self._A[self._n - 1] = None
				self._n -= 1
				return
		raise ValueError("Value not found")
