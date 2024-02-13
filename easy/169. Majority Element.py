# https://leetcode.com/problems/majority-element/description/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num = 0
        max_repetitions = 0
        for el in set(nums):
            if nums.count(el) > max_repetitions:
                max_repetitions = nums.count(el)
                max_num = el
        return max_num


s = Solution()
print(s.majorityElement([3, 1, 3]))
