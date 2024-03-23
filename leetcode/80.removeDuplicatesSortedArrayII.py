# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
from typing import List

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i<2 or num != nums[i-2]:
                nums[i] = num
                i += 1
        return i


if __name__ == "__main__":

    test_cases = [[1]]
    s= Solution()
    for test_case in test_cases:
        print(s.removeDuplicates(test_case))