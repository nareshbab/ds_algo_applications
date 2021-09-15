"""
Stacks and Queues implementation in python
Python methods for solving few of the use cases
ex. reverse a sequence, pattern matching
"""


class Empty(Exception):
	"""Custom exception class for empty Stack and Queue scenarios"""
	pass


class ArrayStack:
	"""Custom implementation of Stacks using Arrays (Last In First Out)
	An Adapter design pattern to abstract out the low level python:list methods
	Methods of Stack:
		push -> Inserts an element into Stack
		pop -> Latest element pushed into Stack
		is_empty -> True/False (Whether Stack is empty or not)
		len -> length of the Stack
		top -> reference to the top element without removing it

	"""

	def __init__(self):
		self._data = []

	def __len__(self):
		"""Returns the length of the Stack"""
		return len(self._data)

	def is_empty(self):
		"""Returns a check whether the Stack is empty or not"""
		return len(self._data) == 0

	def push(self, item):
		"""Inserts an element to stack"""
		self._data.append(item)

	def pop(self):
		"""Returns the top element in the Stack"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data.pop()

	def top(self):
		"""Returns the top element from the Stack without removing it"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data[-1]


def reverse_file(filename):
	"""Overwrite file by reversing its content line by line"""
	S = ArrayStack()
	f = open(filename)
	for line in f:
		S.push(line)

	f.close()

	# Reverse the file
	updated_f = open(filename, 'w')
	# Cannot use for loop iteration since iter method is not defined for the class
	while not S.is_empty():
		updated_f.write(S.pop())

	updated_f.close()

def is_matched(expr):
	"""Returns True if all the delimiters are matched correctly"""

	lefty = '({['
	righty = ')}]'
	S = ArrayStack()
	for c in expr:
		if c in lefty:
			S.push(c)
		elif c in righty:
			if S.is_empty():
				return False
			if righty.index(c) != lefty.index(S.pop()):
				return False
	return S.is_empty()


"""
Queues (FIFO) default methods:
enqueue
dequeue
first
is_empty
len
"""


class ArrayQueue:
	"""Adapter class for defining Queues on top of python lists"""
	DEFAULT_QUEUE_CAPACITY = 10

	def __init__(self):
		"""Creates an empty queue"""

		self._data = [None] * ArrayQueue.DEFAULT_QUEUE_CAPACITY
		self._size = 0
		self._front = 0

	def enqueue(self, item):
		"""Adds an element to the Queue"""
		# Find the index where the new element is to be added
		# IMP:: Its a cyclic list implementation of Queue
		if len(self._data) == self._size:
			self._resize(2 * len(self._data))
		avail = (self._front + self._size) % len(self._data) # Next available slot as per the cyclic list
		self._data[avail] = item
		self._size += 1

	def dequeue(self):
		"""Removes the first element from the Queue"""
		if self.is_empty():
			raise Empty("Queue is empty")
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)  # Cyclic implementation of the Queue
		self._size -= 1
		return answer

	def is_empty(self):
		"""Returns True/False -> if the Queue is empty"""
		return self._size == 0

	def __len__(self):
		"""Returns the length of the Queue"""
		return self._size

	def first(self):
		"""Returns the first element of the Queue"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._data[self._front]

	def _resize(self, new_capacity):
		"""Resizes the array to 2x the default length"""
		B = [None] * new_capacity
		walk = self._front
		for i in range(len(self._data)):
			B[i] = self._data[walk]
			walk = (walk + 1) % len(self._data)
		self._data = B
		self._front = 0
