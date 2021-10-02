import time
from typing import Tuple


def binary_search(arr, target, start=None, end=None) -> Tuple:
	if not start:
		start = 0
	if not end:
		end = len(arr) - 1
	mid = 0
	while start <= end:
		mid = start + (end - start) // 2

		if arr[mid] == target:
			return start, mid, end

		if arr[mid] > target:
			end = mid - 1
		else:
			start = mid + 1
	return start, mid, end


def floor(arr, target):
	"""Returns the greatest number less than target"""
	start, mid, end = binary_search(arr, target)
	return end


def ceiling(arr, target):
	"""Returns the smallest number greater than target"""
	start, mid, end = binary_search(arr, target)
	return start


def next_greatest_letter(arr, target):
	"""
	Returns the next greatest letter from the array of sorted characters
	arr =['a', 'd', 'i', 'j'], target='j', answer = 'a'
	"""
	if target > arr[len(arr) - 1]:
		return -1

	start = 0
	end = len(arr) - 1
	while start <= end:
		mid = start + (end - start) // 2
		if arr[mid] == target:
			return arr[(mid + 1) % len(arr)]
		if arr[mid] > target:
			end = mid - 1
		if arr[mid] < target:
			start = mid + 1

	return arr[start % len(arr)]


def first_last_occurrence_integer(arr, target):
	"""
	Returns the first and the last occurrence of the integer in the array
	arr =[4,5,7,8,8,9] target=8, answer = [3, 4]
	"""
	ans = [-1, -1]

	# check first occurrence
	start = 0
	end = len(arr) - 1

	while start <= end:

		mid = start + (end - start) // 2

		if arr[mid] > target:
			end = mid - 1
		if arr[mid] < target:
			start = mid + 1

		if arr[mid] == target:
			ans[0] = mid
			end = mid - 1

	# check last occurrence
	start = 0
	end = len(arr) - 1

	while start <= end:

		mid = start + (end - start) // 2
		if arr[mid] > target:
			end = mid - 1
		if arr[mid] < target:
			start = mid + 1

		if arr[mid] == target:
			ans[1] = mid
			start = mid + 1

	return ans


def search_in_ordered_infinite_array(arr, target):
	"""Returns the target index in an infinite array"""
	start = 0
	end = 1

	while target > arr[end]:
		new_start = end + 1
		# double the size of array for next iteration
		end = end + (end - start + 1) * 2
		start = new_start
	# TODO:: handle case where the window includes indices that are out of range
	# TODO:: On other not that should never be the case since the array is of infinite length
	return binary_search(arr, target=target, start=start, end=end)


def search_mountain_peak(arr):
	"""
	Returns the peak element from the mountain / bi-tonic array
	arr = [1, 2, 3, 4, 3, 1], ans = 4
	arr = [1,5,9,10,1] ans = 10
	"""
	start = 0
	end = len(arr) - 1
	while start < end:

		mid = start + (end - start) // 2

		if arr[mid] > arr[mid + 1]:
			end = mid
		if arr[mid] < arr[mid + 1]:
			start = mid + 1
	# loop will break once start = end
	# the ans = arr[start] or arr[end]
	return arr[start]


def minimum_index_in_mountain_array(arr, target):
	"""
	Returns the minimum index of the target in the mountain/bi-tonic array
	Assumption that no repetitive elements are present in the array
	"""
	start = 0
	end = len(arr) - 1

	while start < end:
		mid = start + (end - start) // 2
		if arr[mid] > arr[mid + 1]:
			end = mid
		if arr[mid] < arr[mid + 1]:
			start = mid + 1
	# TODO:: we can also handle cases where arr[mid] == arr[mid + 1]
	# loop will break when start = end, so answer = start or end
	max_element_index = start

	start = 0
	end = max_element_index
	while start <= end:

		mid = start + (end - start) // 2
		if arr[mid] > target:
			end = mid - 1
		if arr[mid] < target:
			start = mid + 1
		if arr[mid] == target:
			return mid

	return -1


def get_pivot_in_rotated_sorted_array(arr):
	"""
	Returns the element in the rotated sorted array
	This is rotated or pivoted at an index i.e it is not same as mountain array
	mountain array = [1,2,3,4,2,1], rotated sorted array = [5,6,7,8,0,1,2]
	mountain array = [1,2,3,4,5,1, 0], rotated sorted array = [10,11,12 5,6,7,8]
	therefore peak element approach will not work here, it might
	work for few of the cases but not for all of the cases
	steps:
	1. find the pivot element
	2. search in either of the array
	"""
	start = 0
	end = len(arr) - 1

	while start <= end:

		mid = start + (end - start) // 2
		# case 1: if mid is at the pivot then the next element should be smaller than the mid
		# case 2: if mid is at the pivot + 1, then the previous element should be > then the mid
		# case 3: if start > mid then left hand side is an ascending array
		# we will change end = mid - 1
		# case 4: if start < mid then right hand side is an ascending array
		# we will change start = mid + 1
		if arr[mid] > arr[mid + 1] and mid < end:
			return mid
		if arr[mid - 1] > arr[mid] and mid > start:
			return mid - 1
		if arr[start] > arr[mid]:
			end = mid - 1
		if arr[start] < arr[mid]:
			start = mid + 1

	return -1


def search_rotated_sorted_array(arr, target):
	"""
	Returns the index of target element in rotated sorted array
	"""
	pivot_index = get_pivot_in_rotated_sorted_array(arr)
	s1, m1, e2 = binary_search(arr, start=0, end=pivot_index, target=target)
	if arr[m1] == target:
		return m1
	else:
		s2, m2, e2 = binary_search(arr, start=pivot_index+1, end=len(arr)-1, target=target)
		if arr[m2] == target:
			return m2
		else:
			return -1


def search_rotated_sorted_array_recursive_with_duplicates(arr, start, end, target):
	"""
	Returns the index of the target element in the rotated sorted array
	with duplicates arr[] = {3, 3, 3, 1, 2, 3}, key = 3 , ans = 0
	arr[] = {3, 3, 3, 1, 2, 3}, key = 11 , ans = -1
	"""
	if start > end:
		return -1

	mid = start + (end - start) //2

	if arr[mid] == target:
		return mid

	# handle duplicate case

	if arr[start] == arr[mid] and arr[mid] == arr[end]:
		start += 1
		end -= 1
		return search_rotated_sorted_array_recursive_with_duplicates(arr, start, end, target)

	# If arr[s...mid] is sorted
	if arr[start] <= arr[mid]:

		# As this subarray is sorted we check for the target
		if target >= arr[start] and target <= arr[mid]:
			search_rotated_sorted_array_recursive_with_duplicates(arr, start, mid - 1, target)

		# or we search in the other half of the array
		return search_rotated_sorted_array_recursive_with_duplicates(arr, mid + 1, end, target)

	# If arr[s....mid] is not sorted
	# then the arr[mid.....e] will be sorted
	if target >= arr[mid] and target <= arr[end]:
		search_rotated_sorted_array_recursive_with_duplicates(arr, mid + 1, end, target)

	return search_rotated_sorted_array_recursive_with_duplicates(arr, start, mid -1 , target)


def get_rotation_count_rotated_sorted_array(arr):
	"""
	Returns the count of times the array is rotated
	in short the rotation count = pivot index + 1
	"""
	return get_pivot_in_rotated_sorted_array(arr) + 1


def split_array_largest_sum():
	""""""
	# TODO ::
	pass



# print(first_last_occurrence_integer([2,2,3,4,5,5,5,5], 5))
# print(binary_search([1,2,3,4,5,6], 3))
# print(search_in_ordered_infinite_array([1, 2, 3, 4, 5, 6, 7, 8], 7))
# print(search_mountain_peak([1,2,3,4,5,4,2]))
# print(get_pivot_in_rotated_sorted_array([10,11,12,4,5,6,7]))
# print(get_pivot_in_rotated_sorted_array([4,5,6,7,8,0,1,2]))
# print(get_pivot_in_rotated_sorted_array([6,7,8,0,1,2,3,4,5]))
# print(get_pivot_in_rotated_sorted_array([6,0,1,2,3,4,5]))
# print(search_rotated_sorted_array([6,7,8,9,10,11,12,5], 9))
# print(search_rotated_sorted_array([10,11,12,4,5,6,7], 4))
# print(search_rotated_sorted_array([4,5,6,7,8,0,1,2], 4))
# print(search_rotated_sorted_array([6,0,1,2,3,4,5], 0))
# print(search_rotated_sorted_array_recursive_with_duplicates([ 3, 3, 1, 2, 3, 3 ], 0, 5, 3))
# print(get_rotation_count_rotated_sorted_array([10,11,12,4,5,6,7]))
# print(get_rotation_count_rotated_sorted_array([4,5,6,7,8,0,1,2]))
# print(get_rotation_count_rotated_sorted_array([6,7,8,0,1,2,3,4,5]))
# print(get_rotation_count_rotated_sorted_array([6,0,1,2,3,4,5]))