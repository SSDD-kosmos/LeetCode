# https://leetcode.com/problems/plus-one/description/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        counter = -1
        digits[-1] += 1
        while digits[counter] == 10:
            digits[counter] = 0
            try:
                digits[counter-1] += 1
            except IndexError:
                digits[0] = 0
                digits.insert(0, 1)
            counter -= 1
        return digits


s = Solution()
print(s.plusOne([9]))
