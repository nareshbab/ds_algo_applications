# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:

	@staticmethod
	def removeDuplicates(nums: List[int]) -> int:
		# Solution 1
		i = 0
		n = len(nums)
		for j in range(1, n):
			if nums[j - 1] != nums[j]:
				nums[i] = nums[j]
				i += 1
		return i + 1

		# Solution 2
		# i =0
		# for num in nums:
		# 	if i<1 or num != nums[i-1]:
		# 		nums[i] = num
		# 		i+=1
		# return i

		# Solution 3
		# i = 1
		# for j in range(len(nums) - 1):
		# 	if nums[j] != nums[j+1]:
		# 		nums[i] = nums[j+1]
		# 		i += 1
		# return i


if __name__ == '__main__':

	test_cases = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
	s = Solution()
	for test_case in test_cases:
		print(s.removeDuplicates(test_case))
