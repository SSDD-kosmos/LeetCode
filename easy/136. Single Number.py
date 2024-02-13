# https://leetcode.com/problems/single-number/description/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for el in nums_set:
            if nums.count(el) == 1:
                return el


s = Solution()
print(s.singleNumber([4,1,2,1,2]))
