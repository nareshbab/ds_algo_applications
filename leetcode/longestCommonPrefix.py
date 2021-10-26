# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:

    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        lowest_str = strs[0]
        for i in strs:
            if len(i) < len(lowest_str):
                lowest_str = i
        n = len(lowest_str)
        
        while n:
            flag = 0
            for i in strs:
                if i[0:n] != lowest_str:
                    flag = 1
                    break
            if flag == 1:
                n -= 1
                lowest_str = lowest_str[0:n]
            else:
                return lowest_str
        return ""


if __name__ == '__main__':

    test_cases = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
    s = Solution()
    for case in test_cases:
        print(s.longest_common_prefix(case))
