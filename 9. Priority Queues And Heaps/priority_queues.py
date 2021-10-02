from postitional_list import PositionalList


# Priority Queue implementation using PositionalList extended from Doubly Linked List
class PriorityQueueBase:
	"""
	An interface for Priority Queue
	A queue with key value and weight or priority associated with it
	Methods:
		.add(k, v) add key k with weight/priority of v
		.min()
		.remove_min()
		.is_empty()
		len()
	"""

	class _Item:
		"""Light weight composite to store priority queue items"""
		__slots__ = '_key', '_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __lt__(self, other):
			"""Comparison with other item object"""
			return self._key < other._key

	def is_empty(self):
		"""Returns True/False depending upon queue size"""
		return len(self) == 0


# Creating priority queue on unsorted positional list
# Items are not sorted on the basis of priority
class UnsortedPriorityQueue(PriorityQueueBase):
	"""
	A min oriented Priority queue with unsorted linked list
	Time Complexity:
		.add(k, v)          ->  O(1)
		.min()              ->  O(n)
		.remove_min()       ->  O(n)
		.is_empty()         ->  O(1)
		len()               ->  O(1)
	"""

	def find_min(self):
		"""Returns the min element"""
		if self.is_empty():
			raise ValueError("Priority queue is empty")
		small = self._data.first()
		walk = self._data.after(small)
		while walk:
			if walk.element() < small.element():
				small = walk
			walk = self._data.after(walk)
		return small

	def __init__(self):
		"""Creates new empty unsorted priority queue"""
		self._data = PositionalList()

	def __len__(self):
		"""Returns the size of the queue"""
		return len(self._data)

	def add(self, key, value):
		"""Add a key value pair"""
		self._data.add_last(self._Item(key, value))

	def min(self):
		"""Returns the element with the min priority or weight"""
		p = self.find_min()
		item = self._data.delete(p)
		return item._key, item._value

	def remove_min(self):
		"""Remove the minimum element from the Priority Queue"""
		p = self.find_min()
		item = self._data.delete(p)
		return item._key, item._value


# Creating priority queue on sorted positional list
# Items are sorted on the basis of priority
class SortedPriorityQueue(PriorityQueueBase):
	"""
	A min oriented Priority queue with unsorted linked list
	Time Complexity:
		.add(k, v)          ->  O(n)
		.min()              ->  O(1)
		.remove_min()       ->  O(1)
		.is_empty()         ->  O(1)
		len()               ->  O(1)
	"""

	def __init__(self):
		"""Create an empty priority queue"""
		self._data = PositionalList()

	def __len__(self):
		"""Returns the size of the Priority Queue"""
		return len(self._data)

	def add(self, key, value):
		"""Add an item k with priority/weight v
		head -> 1 -> 2-> .... -> n-1 -> n -> tail
		"""
		newest = self._Item(key, value)
		walk = self._data.last()
		while walk is not None and newest < walk.element():
			walk = self._data.before(walk)
		if walk:
			self._data.add_first(newest)
		else:
			self._data.add_after(walk, newest)
		pass

	def min(self):
		"""Returns the minimum items of the queue"""
		p = self._data.last()
		item = p.element()
		return item._key, item._value

	def remove_min(self):
		"""
		Removes the minimum item from the queue
		Head of the positional list will always be at the min element
		head -> 1 -> 2-> .... -> n-1 -> n -> tail
		"""
		if self.is_empty():
			raise ValueError("Priority Queue is empty")
		item = self._data.delete(self._data.first())
		return item._key, item._value
