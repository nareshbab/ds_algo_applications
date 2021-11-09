# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:

	@staticmethod
	def removeDuplicates(nums: List[int]) -> int:
		i = 0
		n = len(nums)
		for j in range(1, n):
			if nums[j - 1] != nums[j]:
				i += 1
				nums[i] = nums[j]
		return i + 1


if __name__ == '__main__':

	test_cases = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
	s = Solution()
	for test_case in test_cases:
		print(s.removeDuplicates(test_case))
