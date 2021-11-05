class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid - 1
            else:
                start = start + 1
        return start


if __name__ == '__main__':

    test_cases = [([1,3,5,6], 5), ([1,3,5,6], 2), ([1,3,5,6], 7), ([1,3,5,6], 0)]
    s = Solution()
    for test_case in test_cases:
        print(s.searchInsert(test_case[0], test_case[1]))