from priority_queues import PriorityQueueBase


# Priority Queues implemented using array based representation
class HeapPriorityQueue(PriorityQueueBase):
	"""
	A min oriented priority queue implemented using binary heap
	Methods:
		add():                  O(log n)
		remove_min():           O(log n)
		min():                  O(1)
		len():                  O(1)
	"""

	def _parent(self, j):
		"""
		Returns the parent index of j
		j = 2f(p) + 1
		"""
		return (j - 1)//2

	def _left(self, j):
		"""Returns the index of left child of j"""
		return 2*j + 1

	def _right(self, j):
		"""Returns the index of the right child of j"""
		return 2*j +2

	def _has_left(self, j):
		"""Returns True if j has left child otherwise False"""
		return self._left(j) < len(self._data)

	def _has_right(self, j):
		"""Returns True if j has right child otherwise False"""
		return self._right(j) < len(self._data)

	def _swap(self, i, j):
		"""Swaps the elements at indices i and j"""
		self._data[i], self._data[j] = self._data[j], self._data[i]

	def _upheap(self, j):
		"""Moves the elements up"""
		parent = self._parent(j)
		if j > 0 and self._data[j] < self._data[parent]:
			self._swap(j, parent)
			self._upheap(parent)        # recur at position of parent

	def _downheap(self, j):
		"""moves the element down"""
		if self._has_left(j):
			left = self._left(j)
			small_child = left
			if self._has_right(j):
				right = self._right(j)
				if self._data[left] > self._data[right]:
					small_child = right
			if self._data[small_child] < self._data[j]:
				self._swap(j, small_child)
				self._downheap(small_child)
	
	# -------------public behaviours ------------------#
	def __init__(self):
		"""Creates an empty heap based priority queue"""
		self._data = []

	def __len__(self):
		"""Returns the length of the priority queue"""
		return len(self._data)

	def add(self, key, value):
		"""Adds an element to the priority queue"""
		self._data.append(self._Item(key, value))
		self._upheap(len(self._data) - 1)       # up heap newly added item

	def min(self):
		"""Returns the minimum element of the priority queue"""
		if self.is_empty():
			raise ValueError("Priority queue is empty")
		item = self._data[0]
		return item._key, item._value

	def remove_min(self):
		"""Removes the minimum element of the priority queue"""
		if self.is_empty():
			raise ValueError("Priority queue is empty")
		self._swap(0, len(self._data) - 1)
		item = self._data.pop()     # remove the swaped item from the end of the list
		self._downheap(0)
		return item._key, item._value
