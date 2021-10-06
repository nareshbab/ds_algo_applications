# Insertion sort on an array

def insertion_sort(A):
	"""Sorts an array using insertion sort algo"""

	# iterate all elements
	for i in range(1, len(A)):
		curr = A[i]
		j = i
		# if curr is < then shift other elements accordingly
		while j > 0 and A[j-1] > curr:
			A[j] = A[j-1]
			j -= 1
		A[j] = curr
	return A
