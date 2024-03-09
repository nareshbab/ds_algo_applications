"""
Sorting Algorithms
	Insertion sort : O(n2)
	Selection sort : O(n2)
	Bubble sort :   O(n2)
	Heap sort :   O(nlogn)
	Merge sort :    O(nlogn)
	quick sort :   O(nlogn)
	bucket sort:    O(d(n + N))
	radix sort
"""


def insertion_sort(arr):
	"""Sort list of comparable elements into ascending order"""
	for i in range(1, len(arr)):
		curr = arr[i]
		j = i
		while j > 0 and arr[j - 1] > curr:
			arr[j] = arr[j - 1]
			j -= 1
		arr[j] = curr
	return arr


def selection_sort(arr):
	"""
	Selection Sort:
		Time Complexity: O(n2) as there are two nested loops.
		Auxiliary Space: O(1)

	The selection sort algorithm sorts an array by repeatedly finding the
	minimum element (considering ascending order) from unsorted part and
	putting it at the beginning

	arr[] = 64 25 12 22 11

	// Find the minimum element in arr[0...4]
	// and place it at beginning
	11 25 12 22 64

	// Find the minimum element in arr[1...4]
	// and place it at beginning of arr[1...4]
	11 12 25 22 64

	// Find the minimum element in arr[2...4]
	// and place it at beginning of arr[2...4]
	11 12 22 25 64

	// Find the minimum element in arr[3...4]
	// and place it at beginning of arr[3...4]
	11 12 22 25 64
	"""
	for i in range(len(arr)):
		min_index = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]
	return arr


def bubble_sort(arr):
	"""
	Bubble Sort
		Time Complexity: O(n2) as there are two nested loops.
		Auxiliary Space: O(1)

	Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping
	the adjacent elements if they are in wrong order.
	First Pass:
	( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the
	first two elements, and swaps since 5 > 1.
	( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
	( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
	( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are
	already in order (8 > 5), algorithm does not swap them.
	Second Pass:
	( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
	( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
	( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
	( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
	Now, the array is already sorted, but our algorithm does not
	know if it is completed. The algorithm needs one whole pass
	without any swap to know it is sorted.
	Third Pass:
	( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
	( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
	( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
	( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
	"""
	n = len(arr)
	for i in range(n):
		# Last i elements are already in place
		for j in range(0, n - i - 1):
			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr


def heapify(arr, n, i):
	"""
	Arrange elements of an array in binary tree order
		To heapify subtree rooted at index i, n is size of heap
	"""
	largest = i
	left = 2 * i + 1        # (2i + 1)
	right = 2 * i + 2       # (2i + 2)

	# See if left child of root exists and is
	# greater than root
	if left < n and arr[largest] < arr[left]:
		largest = left

	# See if right child of root exists and is
	# greater than root
	if right < n and arr[largest] < arr[right]:
		largest = right

	# Change root, if needed
	if largest != i:
		arr[largest], arr[i] = arr[i], arr[largest]

		# Heapify the root.
		heapify(arr, n, largest)


def heap_sort(arr):
	"""
	Heap Sort:
		Time complexity of heapify is O(Logn).
		Time complexity of createAndBuildHeap() is O(n)
		The overall time complexity of Heap Sort is O(nLogn)

	Heap sort is a comparison-based sorting technique based on Binary Heap data structure.
	It is similar to selection sort where we first find the minimum element and place the
	minimum element at the beginning. We repeat the same process for the remaining elements.
	"""
	n = len(arr)

	# Build a max heap tree
	# [3, 6, 1, 7, 9, 3]
	#   i = 2, left = 5, right = 6
	#   i = 1, left = 3, right = 4
	#   i = 0, left = 1, right = 2
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for j in range(n - 1, 0, -1):
		arr[j], arr[0] = arr[0], arr[j]
		heapify(arr, j, 0)
	return arr


def merge_sort(arr):
	"""
	Merge Sort:
		Time Complexity:    O(nLogn)
		MergeSort(arr[], l,  r)
	If r > l
	1. Find the middle point to divide the array into two halves:
		middle m = l+ (r-l)/2
	2. Call mergeSort for first half:
		Call mergeSort(arr, l, m)
	3. Call mergeSort for second half:
		Call mergeSort(arr, m+1, r)
	4. Merge the two halves sorted in step 2 and 3:
		Call merge(arr, l, m, r)
	"""
	# Return if only single element in array
	if len(arr) <= 1:
		return
	start = 0
	end = len(arr)
	mid = start + (end - start) // 2

	l_arr = arr[:mid]
	r_arr = arr[mid:]

	merge_sort(l_arr)
	merge_sort(r_arr)

	# Iterating elements for final merging
	i = j = k = 0
	while i < len(l_arr) and j < len(r_arr):
		if l_arr[i] < r_arr[j]:
			arr[k] = l_arr[i]
			i += 1
		else:
			arr[k] = r_arr[j]
			j += 1
		k += 1

	# Checking if any element is left
	while i < len(l_arr):
		arr[k] = l_arr[i]
		i += 1
		k += 1

	while j < len(r_arr):
		arr[k] = r_arr[j]
		j += 1
		k += 1
	return arr


def qsort_partition(start, end, arr):
	"""
	This Function handles sorting part of quick sort
	start and end points to first and last element of
	an array respectively
	"""
	pivot_index = start
	pivot = arr[pivot_index]

	# This loop runs till start pointer crosses
	# end pointer, and when it does we swap the
	# pivot with element on end pointer
	while start <= end:

		while start < len(arr) and arr[start] <= pivot:
			start += 1

		while end < len(arr) and arr[end] > pivot:
			end -= 1

		# If start and end have not crossed each other,
		# swap the numbers on start and end
		if start < end:
			arr[start], arr[end] = arr[end], arr[start]
	# Swap pivot element with element on end pointer.
	# This puts pivot on its correct sorted place.
	arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
	return end


def quick_sort(start, end , arr):
	"""
	Quick Sort
		Time Complexity:    O(nLogn)
	QuickSort is a Divide and Conquer algorithm.
	It picks an element as pivot and partitions the given
	array around the picked pivot. There are many different
	versions of quickSort that pick pivot in different ways.

	Always pick first element as pivot.
	Always pick last element as pivot (implemented below)
	Pick a random element as pivot.
	Pick median as pivot.
	"""
	if start < end:
		# p is partitioning index, array[p]
		# is at right place
		p = qsort_partition(start, end, arr)

		# Sort elements before partition
		# and after partition
		quick_sort(start, p - 1, arr)
		quick_sort(p + 1, end, arr)
	return arr


def bucket_sort(arr):
	"""
	Bucket/Radix Sort:
		Time Complexity:    O(d(n+N))
		bucketSort(arr[], n)
	1) Create n empty buckets (Or lists).
	2) Do following for every array element arr[i].
	.......a) Insert arr[i] into bucket[n*array[i]]
	3) Sort individual buckets using insertion sort.
	4) Concatenate all sorted buckets.
	"""
	bucket = []

	# Create empty buckets
	for i in range(len(arr)):
		bucket.append([])

	# Insert elements into respective buckets
	for j in arr:
		# divide the bucket into 10 since the max number is 2 digit
		index_b = int(j / 10)
		bucket[index_b].append(j)

	# Sort elements in each bucket
	for i in range(len(bucket)):
		bucket[i] = sorted(bucket[i])

	# Concatenate all the elements
	k = 0
	for i in range(len(arr)):
		for j in range(len(bucket[i])):
			arr[k] = bucket[i][j]
			k += 1

	return arr


if __name__ == '__main__':
	# print(quick_sort(0, 5, [3, 6, 1, 7, 9, 3]))
	# print(bucket_sort([3, 6, 1, 7, 9, 3]))
	print(insertion_sort([7,8,3,1,2]))
