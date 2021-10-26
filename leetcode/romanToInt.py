# https://leetcode.com/problems/roman-to-integer/submissions/
class Solution:

    @staticmethod
    def roman_to_int(s: str) -> int:
        num_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum_nums = 0
        i = 0
        n = len(s) - 1
        while i <= n:
            if i < n and num_value[s[i+1]] > num_value[s[i]]:
                sum_nums = sum_nums + (num_value[s[i+1]] - num_value[s[i]])
                i += 2
            else:
                sum_nums = sum_nums + num_value[s[i]]
                i += 1
        return sum_nums

if __name__ == '__main__':

    test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    s = Solution()
    for test_case in test_cases:
        print(s.roman_to_int(test_case))