from typing import List

class Solution:

    def merge(self, nums1: List[int], nums2: List[int], m: int, n:int) -> None:
        """
        Do not return anything modify nums1 in place
        """
        # Solution1
        i = m-1
        j = n-1
        k = m+n-1

        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Solution2 - saves memory

        # last = m+n-1

        # while n-1>=0:
        #     if m-1>=0 and nums1[m-1] > nums2[n-1]:
        #         nums1[last] = nums1[m-1]
        #         m -= 1
        #     else:
        #         nums1[last] = nums2[n-1]
        #         n -= 1
        #     last -=1
                



if __name__ == "__main__":

    s = Solution()
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    print(s.merge(nums1, nums2, m, n))