#https://leetcode.com/problems/majority-element

from typing import List

class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        
        # Solution 1
        # max_elements = {}

        # for num in nums:
        #     if num in max_elements:
        #         max_elements[num] += 1
        #     else:
        #         max_elements[num] = 1
        # return max(zip(max_elements.keys(), max_elements.values()))[1]

        # Solution 2 - Moore's Voting Algorithm
        # create ans and count variable
        # iterate nums and increment count if num == ans
        # decrement if num != ans
        # if count becomes 0 then switch ans = current num
        ans = None
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            count += (1 if num == ans else -1)
        return ans


if __name__ == "__main__":

    s= Solution()
    test_cases = [[2,1,2,2,1,1,1,1,3,4]]
    for test_case in test_cases:
        print(s.majorityElement(test_case))