# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:

	@staticmethod
	def removeElement(nums: List[int], val: int) -> int:
		i = 0
		n = len(nums)
		for j in range(n):
			if nums[j] != val:
				nums[i] = nums[j]
				i += 1
		return i


if __name__ == '__main__':

	test_cases = [([3, 2, 2, 3], 3), ([0, 1, 2, 2, 3, 0, 4, 2], 2)]
	s = Solution()
	for test_case in test_cases:
		print(s.removeElement(test_case[0], test_case[1]))
